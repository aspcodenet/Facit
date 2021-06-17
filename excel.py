import xlrd

wb = xlrd.open_workbook("filen.xls")
sheet = wb.sheet_by_index(0)

row = 1
while True:
    if row >= sheet.nrows:
        break
    namn =sheet.cell_value(row, 0) 
    if namn == "":
        break
    team =sheet.cell_value(row, 1) 
    goals =int(sheet.cell_value(row, 2) )
    assists =int(sheet.cell_value(row, 3) )
    points =int(sheet.cell_value(row, 4))
    print(f"{namn} {team} {goals}+{assists}={points}")
    row = row + 1
