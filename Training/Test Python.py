import pandas as pd

file_path = r'C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\2026\Training\Test Python Excel.xlsx'
excel_file = pd.ExcelFile(file_path)
print("Sheet names: ")
for index, sheet in enumerate(excel_file.sheet_names):
    print(index, sheet)

print('\n')
print('This should be row 6')
row = pd.read_excel(excel_file, sheet_name = 6, usecols=['PR ID']).iloc[0:15]
print(row)



