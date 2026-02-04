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


"""
This returns the entire row
mask = df.apply(lambda row: row.astype(str).str.contains(str(pr_767509), na=False)).any(axis=1)
rows_with_value = df[mask]
print(rows_with_value)
"""
for i, col in enumerate(training_sheet.columns):
    print(i, col)

pr_767509 = 767509
###

pr_stamp = pd.read_excel(
    excel_file, 
    sheet_name = 0, 
    usecols=[0]
    ).iloc[0:5]
print(pr_stamp)

"""pr_list = pr_stamp.tolist()
print(pr_list)"""

print('\n\n')

###

print("Sheet names: ")
for index, sheet in enumerate(excel_file.sheet_names):
    print(index, sheet)
print('\n\n')


"""
    .iloc - method to print certain rows 
    uscols = parameter to print the column you name 

column = pd.read_excel(excel_file, sheet_name = 7, usecols=['PR ID']).iloc[0:15]
print(column)

| Thing you see | Actual type       | How to listify |
| ------------- | ----------------- | -------------- |
| Excel column  | `Series`          | `.tolist()`    |
| NumPy array   | `ndarray`         | `.tolist()`    |
| Cell value    | scalar            | wrap in `[]`   |
| Series loop   | labels by default | use `.values`  |


| Excel thing     | pandas type |
| --------------- | ----------- |
| Worksheet range | DataFrame   |
| Single column   | Series      |
| Single cell     | scalar      |

"""