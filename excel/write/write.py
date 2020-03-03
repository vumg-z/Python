import openpyxl, os

os.chdir(r"C:\Users\Billy\Desktop\B\Python/excel")

wb = openpyxl.Workbook()

sheet = wb.active

sheet.title = 'Say mane'

wb.save('example.xlsx')