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
    if "QC" in item_ID:
        print(item_ID)