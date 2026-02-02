import pandas as pd

file_path = r'C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\2026\Training\Test Python Excel.xlsx'
excel_file = pd.ExcelFile(file_path)
print("Sheet names: ")
for index, sheet in enumerate(excel_file.sheet_names):
    print(index, sheet)