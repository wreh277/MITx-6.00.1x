# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:22:23 2022

@author: HP15-DA0013LA
"""

s="abcbcd"

z="abcdefghijklmnopqrstuvwxyz"
orden0=0
orden1=0
palabra0=""
palabra1=""

for i in range(0,len(s)):
    for j in range(0,len(z)):
        if z[j]==s[i]:
            orden1=j
            print(orden1)
           
    if orden1>=orden0:
        orden0=orden1 
        palabra1+=s[i]
        if len(palabra1)>len(palabra0):
            palabra0=palabra1
            print(palabra0)
    else:
        orden0=orden1
        palabra1=s[i]
print("Longest substring in alphabetical order is:",palabra0)
            
