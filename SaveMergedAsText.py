import numpy as np
import pandas as pd

pre = "Data/Datenbank/Excel/"
ending = ".xlsx"

df_merged = pd.read_excel(pre + "Merged_DB" + ending)

file = open("MedicineInfo.txt", "w")

for index_row, row in df_merged.iterrows():
    medicineInfo = ""
    for i in range(0,len(df_merged.columns)):
        if str(df_merged.iloc[index_row,i]) == "nan":
            medicineInfo += ""
        else:
            medicineInfo += str(df_merged.iloc[index_row,i])
            medicineInfo += " "
    file.write(medicineInfo + "\n")
    file.write(" ")

file.close()