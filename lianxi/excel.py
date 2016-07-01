#-*-coding:utf-8-*-

'''学习如何读写excel中的数据，使用到的模块有xrld、xlwt、xlutis'''
import xlrd,xlwt

from xlutils.copy import copy

font = xlwt.easyxf('font:color-index red ,bold on')
headerStyle = font
oldwb = xlrd.open_workbook('erpdata1.xls',formatting_info=True)  #保持原excel文档格式不变
newwb = copy(oldwb)   #copy从打开的xlrd的book变量中，拷贝出一份成为新的xlwt的WorkBook变量
newws = newwb.get_sheet(2)   #通过get_sheet去获得对应的sheet
newws.write(1,6,'通过'.decode('gbk'))    #写入新数据，注意此处中文必须解码
#写入完成后，需要保存
newwb.save('erpdata1.xls')
