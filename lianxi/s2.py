#coding:utf-8
from selenium import webdriver
import xlrd
from lianxi import s3
def setTable(filepath, sheetname):
    """
    filepath:文件路径
    sheetname：Sheet名称
    """
    data = xlrd.open_workbook(filepath)
    #通过索引顺序获取Excel表
    table = data.sheet_by_name(sheetname)
    return table

#读取xls表格，使用生成器yield进行按行存储
def getTabledata(filepath, sheetname):
    """
    filepath:文件路径
    sheetname：Sheet名称
    """
    table = setTable(filepath, sheetname)
    for args in range(1, table.nrows):
        #使用生成器 yield
        yield table.row_values(args)

#获取单元格数据
def getcelldata(sheetname, RowNum, ColNum):
    """
    sheetname:表格Sheets名称
    RowNum:行号 从0开始
    ColNum:列号 从0开始
    """
    table = setTable('erpdata1.xls',sheetname)
    celldata = table.cell_value(RowNum, ColNum)
    return  celldata

loc = getcelldata('case data',1,6)

print s3.num


# data = xlrd.open_workbook('erpdata1.xls')
# loc = data.sheet_by_name('case data')
# loc.write(1,6,0)
