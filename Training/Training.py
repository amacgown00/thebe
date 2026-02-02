from pathlib import Path
import csv

path = Path(r"C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\2026\Training\no suffix BPG 2024_SFLMS Object Creation Template(Learning Items).csv")
lines = path.read_text(encoding="cp1252", errors="replace").splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#for index, column_header in enumerate(header_row):
 #   print(index, column_header)

itemID_list = []  #create a new variable
for row in reader: #new variable row, reader variable links to the import csv method
    #trace the string of variables that narrows the information you want
    item_ID = (row[2])
    itemID_list.append(item_ID)
    print(item_ID)

import pandas as pd
excel_file = pd.ExcelFile('mega training.xlsx')

df0=pd.read_excel(excel_file, sheet_name='WD IDs')
df1=pd.read_excel(excel_file, sheet_name='START HERE')
df2=pd.read_excel(excel_file, sheet_name='Learning Items')
df3=pd.read_excel(excel_file, sheet_name='Content Items')
df4=pd.read_excel(excel_file, sheet_name='Multiple Content Items')
df5=pd.read_excel(excel_file, sheet_name='SubCurriculum Object')
df6=pd.read_excel(excel_file, sheet_name='SubCurriculum Contents')
df7=pd.read_excel(excel_file, sheet_name='Completions')
df8=pd.read_excel(excel_file, sheet_name='Curriculum Object')
df9=pd.read_excel(excel_file, sheet_name='Curriculum Contents ')
df10=pd.read_excel(excel_file, sheet_name='Global Training Items')
df11=pd.read_excel(excel_file, sheet_name='Content Items with Quizzes')
df12=pd.read_excel(excel_file, sheet_name='Assignment Profiles')
df13=pd.read_excel(excel_file, sheet_name='Assignment Profile Assignments')
df14=pd.read_excel(excel_file, sheet_name='OBS')
df15=pd.read_excel(excel_file, sheet_name='Roles 4 Training')
df16=pd.read_excel(excel_file, sheet_name='Sheet1')
df17=pd.read_excel(excel_file, sheet_name='Lists')

output_df=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17], ignore_index=True)

output_df.to_csv("mergedtraining.csv",index=False)