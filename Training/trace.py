import pandas as pd

file_path = r"C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\2026\Training\mega training.xlsx"

xls = pd.ExcelFile(file_path)
sheet_list = xls.sheet_names



for each_line in sheet_list:
    print(f"df-pd.read_excel(excel_file, sheet_name='{each_line}'")

for index, header in enumerate(sheet_list):
    print(index, header)

    
number = [str(i+1) for i in range(len(sheet_list))]
print(f"df{number}-pd.read_excel(excel_file, sheet_name='{each_line}'")