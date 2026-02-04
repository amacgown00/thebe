import pandas as pd

file_path = r'C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\2026\Training\Test Python Excel.xlsx'

excel_file = pd.ExcelFile(file_path)
training_sheet = pd.read_excel(excel_file, sheet_name = 0)

df = pd.read_excel(file_path, sheet_name=0)
lookup_value = "CUR-LSG-BED-GEN-0004"
result = df.loc[
    df["Sub-Curriculum ID"].astype(str).str.contains(str(lookup_value), na=False),"Curriculum ID"
]

if not result.empty:
    print(result.iloc[0])
else:
    print('No match found')
