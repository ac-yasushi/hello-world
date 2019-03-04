# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:09:11 2018

@author: tgvuhn
"""

with open("C:/Users/tgvuhn/OneDrive/HTML/CBT_form.html", "rb") as f:
    string=f.readlines()

s=""

for i in range(len(string)):
    s = string[i]
    print(s.decode("utf-8"))

