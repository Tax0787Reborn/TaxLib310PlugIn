import sys
w=sys.argv[1]
a=open(w).read()
a=a.replace('case _:','else:') #의미 정리
a=a.replace('case ','if match==')
a=a.replace('match ','match=')
e=''
f=0
g=1
for _ in a.split('\n'):
    if ('match='in _) and (not ('if match==' in _)) and g:
        f=0
        b=''
        c=1
        z=_.split('match=')[0]
        d=_.replace(':',f'\n{z}if 1:')
        g=0
    elif 'if match==' in _ and f:
        d=_.replace('if match==','elif match==')
    elif 'if match==' in _:
        d=_
        f=1
    elif 'else:'in _:
        f,g=0,1
        d=_
    else:
        d=_
    e+=d+'\n'
open(w+'.py','w').write(e)