#-*-coding:utf-8-*-
import xlrd,xlwt

wfile = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet1 = wfile.add_sheet('sheet_01',cell_overwrite_ok=True)
style = xlwt.easyxf('pattern:pattern solid,fore_colour ocean_blue;font:height 400,colour_index green,bold on')

row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
column0 = [u'机票',u'船票',u'火车票',u'汽车票',u'其它']
status = [u'预订',u'出票',u'退票',u'业务小计']
for i in range(len(row0)):
    sheet1.write(0,i,row0[i],style)

style2 = xlwt.easyxf('font:height 200,colour_index light_blue')

i = 1
j = 0
while i < 4*len(column0) and j < len(row0):
    sheet1.write_merge(i,i+3,0,0,column0[j],style2)
    sheet1.write_merge(i,i+3,7,7)
    i += 4
    j += 1

i = 1
while i < 5*len(status):
    for j in range(len(status)):
        print j,status[j]
        sheet1.write(j+i+1,1,status[j])
    i += 4

sheet1.write(21,0,u'合计')

wfile.save('ssss11.xls')

rfile = xlrd.open_workbook('ssss11.xls')
sheet = rfile.sheet_by_index(0)
rows = sheet.row_values(1)
cols = sheet.col_values(0,sheet.ncols)
print 'rows:',rows
print 'cols:',cols

cell = sheet.cell_value(1,1)
cell1 = sheet.cell(1,1).value
print 'cell:',cell
print 'cell1:',cell1