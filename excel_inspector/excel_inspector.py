# Parse spreadsheets and its sheets ===========================================
import pandas as pd
import os

# add your folder path
sheets_folder = r''

for path, subdirs, files in os.walk(sheets_folder):
    for filename in files:
        print('\n [] File:', filename, '===============')
        if filename.endswith('.xlsx'):
            excel = pd.ExcelFile(path + '\\' + filename)
            print('Number of sheets:', len(excel.sheet_names))
            print('Sheet names:', excel.sheet_names)
            for sheet in excel.sheet_names:
                df = excel.parse(sheet)
                print('Sheet:', sheet, ' with the columns:', list(df.columns))
