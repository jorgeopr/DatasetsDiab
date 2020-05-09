#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 07:04:59 2019

@author: abielroche
"""

f_input = open("diabetes.txt",'r')
f_output = open("diabetes.txt-clean-data.csv", 'w')
for line in f_input:
    if '?' not in line:
        new_output_line = line.replace(";"  ,   ",")
        f_output.write(new_output_line)

f_input.close()
f_output.close()

print("End processing")