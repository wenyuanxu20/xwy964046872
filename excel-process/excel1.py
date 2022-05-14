# coding = utf-8

from openpyxl import Workbook
from openpyxl import load_workbook



#实例化 + 创建并保存excel文件
wb = Workbook()

sheet = wb.active
print(sheet)
print(sheet.title)
sheet.title = 'page 1'
print(sheet.title)
wb.save('test1.xlsx')


# open
path = 'C:\\Users\\Wenyuan Xu\\Desktop\\excel-process\\test1.xlsx'
wb2 = load_workbook('test1.xlsx')
wb3 = load_workbook(path)
print(wb2)
sheet3 = wb3.active
print('sheet3: ', sheet3)


#sheet.title = 'test1' #change name