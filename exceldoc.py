import itertools

import pandas
import pandas.io.excel as excel
import xlrd


class ExcelDocument(excel.ExcelFile):
    """ Wrapper around the `excel.ExcelFile` class. """
    
    def __getitem__(self, name):
        """ Gets a sheet by name. """
        if name in self.sheet_names:
            return ExcelSheet(self.book.sheet_by_name(name))
        else:
            raise KeyError('Invalid sheet name "%s"' % name)
            
    def __iter__(self):
        """ Iterates over the sheets in the document. """
        for name in self.sheet_names:
            yield ExcelSheet(self.book.sheet_by_name(name))
            
    def __len__(self):
        """ Number of sheets in the document. """
        return self.book.nsheets
      
    @property
    def global_names(self):
        """ Lists all global names. """
        return { name : self.book.name_map[name] \
            for name, scope in self.book.name_and_scope_map \
            if scope == -1 }


class ExcelSheet:
    """ Class that represents an Excel sheet. """
    
    def __init__(self, sheet, has_header=True):
        
        def find_sheet_idx(sheet):
            idx = -1
            for sh in sheet.book.sheets():
                idx += 1
                if sh.name == sheet.name:
                    break
            if idx == -1:
                raise ValueError("Couldn't locate sheet %s." % sheet.name)
                
            return idx
            
        self._sheet = sheet
        self._has_header = bool(has_header)
        self._sheet_idx = find_sheet_idx(sheet)
        
    def iter_rows(self):
        """ Iterates over the rows of data, skipping the header. """
        start = 1 if self._has_header else 0
        for r in range(start, self._sheet.nrows):
            yield [ xlrd.xldate.xldate_as_datetime(c.value, 0).date() \
                if c.ctype == xlrd.XL_CELL_DATE else c.value \
                for c in self._sheet.row(r) ]
                
    def data_frame(self):
        """ Build a `pandas` data frame from all named ranges. """
        
        def column_from_range(named_range):
            sh, rlo, rhi, clo, chi = named_range.area2d()
            return [ sh.cell(r, clo).value \
                for r in range(rlo, rhi) ]
                
        ranges = self.named_ranges
        return pandas.DataFrame(
            { name : column_from_range(ranges[name]) \
            for name in ranges })
                
    def iter_named_ranges(self):
        """ Iterates over rows of data using named ranges. """
        
        def iter_single_range(named_range):
            sh, rlo, rhi, clo, chi = named_range.area2d()
            for r in range(rlo, rhi):
                yield sh.cell(r, clo).value
                
        ranges = self.named_ranges
        header = tuple(ranges.keys())
        for row in itertools.zip_longest(
            *[ iter_single_range(ranges[name]) for name in ranges ]):
            yield { key : value for key, value in zip(header, row) }
    
    @property
    def name(self):
        return self._sheet.name
        
    @property
    def nrows(self):
        return self._sheet.nrows
        
    @property
    def ncols(self):
        return self._sheet.ncols
        
    def __getitem__(self, n):
        """ Returns the `n`-th row. """
        if not (0 <= n < self.nrows):
            raise ValueError('0 >= row > %d, but %d given.'
                % (self.nrows, n))
        return self._sheet.row(n)
        
    def __iter__(self):
        """ Iterates over all cells left to right, top to bottom. """
        for r in range(self.nrows):
            for c in range(self.ncols):
                yield self._sheet.row(r)[c].value
       
    @property
    def local_names(self):
        """ List all local names. """
        return { name : self._sheet.book.name_and_scope_map[(name, scope)] \
            for name, scope in self._sheet.book.name_and_scope_map \
            if scope == self._sheet_idx }
            
    @property
    def named_ranges(self):
        """ List of all named ranges for this sheet. """
        names = self.local_names
        return { name: names[name] \
            for name in names \
            if names[name].result.kind in (xlrd.oREF, xlrd.oREL) }