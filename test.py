# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:09:11 2018

@author: tgvuhn
"""

with open("hoge", "rb") as f:
    string=f.readlines()

s=""

for i in range(len(string)):
    s = string[i]
    print(s.decode("utf-8"))

