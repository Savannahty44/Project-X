# -*- coding: utf-8 -*-
"""
@author: Savannah T
"""

import os 
import pandas as pd


for root, directory, files in os.walk(r'C:\Users\Savannah\Google Drive\Savannah\Project X'):
    for f in files:
        filename = os.path.join(root, f)
        df = pd.read_excel(filename)
        value = df['E/S'][3]
        xls = pd.ExcelFile(filename)
        df_lancamentos = pd.read_excel(filename, sheetname = 0, skiprows= 3)
        print(df_lancamentos)
        #what up hoe
        

    
        
