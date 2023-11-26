import pandas as pd
# import openpyxl
import xlsxwriter
import numpy as np
import glob

all_data = pd.DataFrame()
for f in glob.glob('*.xlsx'):
   df = pd.read_excel(f)
   all_data = all_data.concat(df, ignore_index=True)



writer = pd.ExcelWriter('mycollected_data.xlsx', engine='xlsxwriter')
all_data.to_excel(writer, sheet_name='Sheet1')
writer.save()
