#-*-coding:utf-8-*-

'''ѧϰ��ζ�дexcel�е����ݣ�ʹ�õ���ģ����xrld��xlwt��xlutis'''
import xlrd,xlwt

from xlutils.copy import copy

font = xlwt.easyxf('font:color-index red ,bold on')
headerStyle = font
oldwb = xlrd.open_workbook('erpdata1.xls',formatting_info=True)  #����ԭexcel�ĵ���ʽ����
newwb = copy(oldwb)   #copy�Ӵ򿪵�xlrd��book�����У�������һ�ݳ�Ϊ�µ�xlwt��WorkBook����
newws = newwb.get_sheet(2)   #ͨ��get_sheetȥ��ö�Ӧ��sheet
newws.write(1,6,'ͨ��'.decode('gbk'))    #д�������ݣ�ע��˴����ı������
#д����ɺ���Ҫ����
newwb.save('erpdata1.xls')
