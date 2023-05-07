o=open
a='TaxSetting'
with o(a+'.sh')as f1:
    with o(a+'.bat','w')as f2:
        f2.write('''\
@echo off
'''+f1.read())