o=open
a='TaxSetting'
with o(a+'.sh')as f1:
    a=f1.read()
    a.replace('@echo off','#!/bin/sh')
    with o(a+'.bat','w')as f2:
        f2.write(a)
