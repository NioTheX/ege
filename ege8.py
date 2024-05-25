import itertools
k=0
for i in itertools.product('01234567',repeat=8):#repeat не r !
    s=''.join(i)
    f=True
    for j in range(7):
        if (  int(s[j])%2==0 and int(s[j+1])%2==0  ) or (  int(s[j])%2==1 and int(s[j+1])%2==1  ):
            f=False
            break
    if s[0]!='0' and len(s)==len(set(s)) and f : # s[0]!='0'
        k+=1
print(k)

#####

import itertools
k=0
for i in itertools.product('ПИРОГ',repeat=6):
    s=''.join(i)
    if s.count('Р')==1 and s.index('Р')!=5:
            if s[s.index('Р')+1] in'ИО':
                k+=1
print(k)