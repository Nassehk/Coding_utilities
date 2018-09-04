# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:51:24 2018
This module import phase data from an excel file. The current data supported are CTE and maximum temperature for the phase to exist.
CTE is written in the format of polynomial coefficients separated by coma (,). Enter as a,b,c, for polunomial  ax^(n)+bx^(n-1)+ ... . Poly coefs must end with a comma. This is to make sure data type is string.

@author: nkhodaie
"""

import pandas as pd
import numpy as np

def import_phases(file_name):
    class phase(object):
        def __init__(self,CTE,max_temp):
            self.CTE=CTE
            self.max_temp=max_temp



#    file_name='phase_data.xlsx'
    data=(pd.read_excel(file_name,sheet_name=None))
    master=data[data.keys()[0]]

    property_names=list(master)[:-1]
#    for prop in property_names:
#        if 'cte' in prop.lower():
#            cte_column_name=prop
    #        print ('yes')
#    phase_names=master.index.values

    #for phase_name in phase_names:
    #    master[cte_column_name][phase_name]=(master[cte_column_name][phase_name]).split(',')

    master_phases_data={}
    for phase_name in master.index.values:
        cte=master[property_names[0]][phase_name].split(',')[:-1]
        cte=map(np.float,cte)
        max_temp=master[property_names[1]][phase_name]
        master_phases_data[phase_name]=phase(cte,max_temp)
    return master_phases_data

