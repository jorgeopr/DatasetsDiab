# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:09:34 2020

@author: jorge
"""

f_input = open("liver_patient.txt", 'r')
f_output = open("liver_patient_clean_data.csv", 'w')
for line in f_input:
    if '?' not in line:
        new_output_line = line.replace (";" , ",")
        f_output.write(new_output_line)
        
f_input.close()
f_output.close()

print("End Process")
        