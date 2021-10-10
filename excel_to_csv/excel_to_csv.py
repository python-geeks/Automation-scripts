import openpyxl
import csv

print("Enter Path of your Excel file")
xls_file = input()
csv_file = 'mycsvfile.csv'
mode = 'w'

wb = openpyxl.load_workbook(xls_file)
sh = wb.active
with open(csv_file, mode, newline="") as f:
    col = csv.writer(f)
    for row in sh.rows:
        col.writerow([cell.value for cell in row])
