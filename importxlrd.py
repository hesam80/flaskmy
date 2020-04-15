import xlrd , numpy
import numpy as np
wb=xlrd.open_workbook('tst.xlsx')
sheet=wb.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
g= numpy.array([])
for i in range(sheet.ncols):
	for j in range(sheet.nrows):
		#print(sheet.cell_value(j, 0))
		g = numpy.array([[sheet.nrows,sheet.ncols],[i,j],[sheet.cell_value(0, i),sheet.cell_value(j, 0)]])
		print("g=",g)
		print(g.shape)
# for i in range(sheet.ncols):
# 	for j in range(sheet.nrows):
		
# 		print(sheet.cell_value(j, i))
# 		z=np.array(sheet.cell_value(j,i))
# 		z = hstack((z,z))
# 		print("z= ",z)
  
#z=np.array(sheet.cell_value(j,i)).reshape((sheet.ncols,sheet.nrows))
		#print("z= ",z)
print("g=",g)