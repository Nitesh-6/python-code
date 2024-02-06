import xlrd

wb = xlrd.open_workbook("matches.xlsx")
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(0, 0))

row_count = sheet.nrows
col_count = sheet.ncols
row = []
for i in range(row_count):
    for j in range(col_count):
        row.append(sheet.cell_value(i, j))
print(row)
