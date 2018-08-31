# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:23:18 2018
imports settings as a dictionary from a .xlsx file. The excel file must have three columns. In the first row the first element must be empty the second cell must have 'value' written in it without quotes. The third cell must have 'help' written in it.
The setting names are listed in the first column starting from second row. cell [A1] must be empty in the excel file.
@author: nkhodaie
"""
import pandas as pd
def importer(file_name):
    AA={}
    data=(pd.read_excel(file_name,sheet_name=None))
    settings=data[data.keys()[0]]
    setting_names_list=list(settings.index.values)
    column_names=list(settings)
    for item in setting_names_list:
        AA[item]=settings[column_names[0]][item]
    return AA