import openpyxl
import os

os.chdir(r"C:\Users\Billy\Desktop\B\Python/excel/filter")

wb = openpyxl.load_workbook(
    'REPORTE IEPS 2019 cuarto trim macario filtra - Copy.xlsx')

# imprimir columna de contenido
sheetname = wb.sheetnames[3]

sheet = wb[sheetname]

for row in range(2, 1017):
    string = sheet['F' + str(row)].value
    if(string is not None):
        if("LTO" in string or "MIL" in string or "LTS" in string or "LTOS" in string or "ML" in string or "L" in string):
            sheet['G' + str(row)] = "bote"
        elif("KG" in string or "GR" in string or "K" in string or "LB" in string or "G" in string):
            sheet['G' + str(row)] = "bolsa"

wb.save('REPORTE IEPS 2019 cuarto trim macario filtra - Copy.xlsx')
