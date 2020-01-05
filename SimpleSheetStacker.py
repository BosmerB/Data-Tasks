# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 07:56:03 2019

@author: blee
"""
"""
Simple script to stack Excel sheets from a workbook.
Useful for instances where data tables with identical columns have been
provided across multiple sheets.
"""


import pandas as pd 

filepath = 'filepath.xlsx'

#creating Excel file object and sheetname list
xls_obj = pd.ExcelFile(filepath)
sheet_names = xls_obj.sheet_names

#list of dataframes created for each list
sheet_dfs = [pd.read_excel(xls_obj, sheet) for sheet in sheet_names]

#stacking dfs and resetting index
stacked_sheets = pd.concat(sheet_dfs).reset_index(drop=True)
  
#exporting as pipe-limited file
stacked_sheets.to_csv('filepath.txt', 
                      sep = '|', index=False)
