# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:23:51 2019

@author: SHREYAS
"""
lst=[]
ln=0
flag=0
fn=input("Enter Filename")

fh=open(fn)

for line in fh:
    for word in line.split():
        lst.append(word)
print(lst)
large=lst[0]
for wd in lst:
    if len(wd)>ln:
        large=wd
print("Largest word is:"+large)


            
