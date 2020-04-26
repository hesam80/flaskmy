""" excel_tutorial.py
Source code for the Excel tutorial.

author: Alberto Semat, contributing writer for wellsr.com
version: 1.0.0 [2019-04-01]
"""

import datetime
import sqlite3
import random
import os.path

import pandas
import xlrd

from exceldoc import *


def test_sep(title):
    """ Prints a separator. """
    print(title.center(50, '-'))


# ======================== Excel Types Conversion =============================

def test_xlrd_datetime_functions():
    """ Test all function from the `xlrd.xldate` module. """
    # Get the current date and time
    today_ms = datetime.datetime.now()
    today = datetime.datetime(*today_ms.utctimetuple()[ : 6])
    # Converts a `tuple` date into a `float` date
    fdate = xlrd.xldate.xldate_from_date_tuple(today.utctimetuple()[:3], 0)
    # Converts a `tuple` time into a `float` time
    ftime = xlrd.xldate.xldate_from_time_tuple(
        (today.hour, today.minute, today.second))
    # Converts a `tuple` date and time into a `float` date and time
    fdatetime = xlrd.xldate.xldate_from_datetime_tuple(
        today.utctimetuple()[ : 6], 0)
    # Converts a `float` date into a tuple
    tdate = xlrd.xldate.xldate_as_tuple(fdatetime, 0)
    # Converts a `float` date into a `datetime.datetime` object.
    date = xlrd.xldate.xldate_as_datetime(fdatetime, 0)
    print('Today is %s' % today)
    print('float date is %.3f (%s)' \
        % (fdate, xlrd.xldate.xldate_as_datetime(fdate, 0)))
    print('float time is %.3f (%s)' \
        % (ftime, xlrd.xldate.xldate_as_datetime(ftime, 0)))
    print('float datetime is %.3f' % fdatetime)
    print('date tuple is ', tdate)
    print('today == date? %s' % (today == date))
    print('today == datetime.datetime(*tdate)? %s' \
        % (today == datetime.datetime(*tdate)))


        
# =================== Case Study 1: Plain Excel Sheet =========================
        
def build_case_study_1_table():
    """ Builds a table for case study 1. """
    with sqlite3.connect('albums.db3') as db:
        db.execute(
            "CREATE TABLE IF NOT EXISTS albums(" \
            "id INTEGER PRIMARY KEY," \
            "nr INTEGER NOT NULL," \
            "band TEXT NOT NULL," \
            "song TEXT NOT NULL," \
            "album TEXT NOT NULL," \
            "duration TEXT NOT NULL);")
            
        db.commit()
                
def case_study_1():
    """ Test for case study 1. """
    # Open the database connection and the Excel file
    with sqlite3.connect('albums.db3') as db, \
        ExcelDocument('albums.xlsx') as src:
        insert_template = "INSERT INTO albums " \
            "(nr, band, song, album, duration) " \
            "VALUES (?, ?, ?, ?, ?);"
            
        # Clear the database
        db.execute('DELETE FROM albums;')
        
        # Load data from each Excel sheet into the database
        for sheet in src:
            try:
                db.executemany(insert_template, sheet.iter_rows())
            except sqlite3.Error as e:
                print(e)
                db.rollback()
            else:
                db.commit()
        
        # Check if all data have been loaded
        select_stmt = 'SELECT DISTINCT band, album FROM albums;'
        for row in db.execute(select_stmt).fetchall():
            print(';'.join(row))
            


# ====================== Case Study 2: Named Ranges ===========================

def build_case_study_2_table():
    """ Builds a table for case study 2. """
    with sqlite3.connect('albums-named.db3') as db:
        db.execute(
            "CREATE TABLE IF NOT EXISTS albums(" \
            "id INTEGER PRIMARY KEY," \
            "nr INTEGER NOT NULL," \
            "band TEXT NOT NULL," \
            "song TEXT NOT NULL," \
            "album TEXT NOT NULL," \
            "duration TEXT NOT NULL);")
            
        db.commit() 
                    
def case_study_2():
    """ Test for case study 2. """
    # Open the database connection and the Excel file
    with sqlite3.connect('albums-named.db3') as db, \
        ExcelDocument('albums-named.xls') as src:
        insert_template = "INSERT INTO albums " \
            "(nr, band, song, album, duration) " \
            "VALUES (:nr, :band, :song, :album, :duration);"
            
        # Clear the database
        db.execute('DELETE FROM albums;')
        
        # Load data from each Excel sheet into the database
        for sheet in src:
            try:
                db.executemany(insert_template, sheet.iter_named_ranges())
            except sqlite3.Error as e:
                print(e)
                db.rollback()
            else:
                db.commit()
        
        # Check if all data have been loaded
        select_stmt = 'SELECT DISTINCT band, album FROM albums;'
        for row in db.execute(select_stmt).fetchall():
            print(';'.join(row))

# ===================== Case Study 3: Pivot Tables ===========================

def generate_case_study_3_data():
    """ Generate data for case study 3. """
    today = datetime.datetime.now()
    MAX_DAY = (0,
        31, 28, 31, 30,
        31, 30, 31, 31, 
        30, 31, 30, 31)
    MAX_INCOME, MIN_INCOME = 999, 200
    SELLERS = ('John', 'Matthew', 'Annie', 'Mark', 'Ian', 'Nina')
    NRECORDS = 100
    
    def generate_date():
        """ Generate a date for the `date` field. """
        month = random.randint(1, today.month)
        return datetime.datetime(
            today.year, month, 
            random.randint(1, MAX_DAY[month])).date()
        
    def generate_income():
        """ Generate a value for the `income` field. """
        return '$%d.00' % random.randint(MIN_INCOME, MAX_INCOME)
        
    def generate_seller():
        """ Pick a seller. """
        return random.choice(SELLERS)
        
    def generate_record():
        """ Generate a record on the data source. """
        return '"%s","%s","%s"\n' \
            % (random.choice(DATES), generate_seller(), generate_income())
        
    DATES = [ generate_date() for i in range(10) ]
    if not os.path.exists('pivot-data.csv'):
        with open('pivot-data.csv', 'wt') as file:
            file.write('"Date","Seller","Income"\n')
            for i in range(NRECORDS):
                file.write(generate_record())
    
def case_study_3():
    """ Test for case study 3. """
    with ExcelDocument('pivot.xls') as src:
        table = pandas.pivot_table(
            src['pivot-data'].data_frame(),
            columns = 'month',
            values = 'income',
            index = 'seller',
            aggfunc = {'income' : sum},
            fill_value = 0 )
        print(table)
            
# =============================== TEST ========================================

def test_excel_types():
    """ Tests all functions dealing with type conversion. """
    test_sep('xlrd.xldate Functions')
    test_xlrd_datetime_functions()

def test_case_study_1():
    """ Tests the first case study (simple Excel sheet). """
    build_case_study_1_table()
    case_study_1()
    
def test_case_study_2():
    """ Tests the second case study (sheet with named ranges). """
    build_case_study_2_table()
    case_study_2()
    
def test_case_study_3():
    """ Tests the third case study (sheet with pivot table). """
    generate_case_study_3_data()
    case_study_3()
    
def test_all_case_studies():
    """ Tests all case studies. """
    test_sep('Simple Excel Sheet')
    test_case_study_1()
    test_sep('Excel Sheet with Named Ranges')
    test_case_study_2()
    test_sep('Excel Pivot Table')
    test_case_study_3()
    
def test_all():
    """ Execute all tests. """
    test_excel_types()
    test_all_case_studies()


test_case_study_1()
