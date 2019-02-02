name1,m11,m12,m13 = map(str,input().split('#'))
name2,m21,m22,m23 = map(str,input().split('#'))
x1 = int(m11)+int(m12)+int(m13)
x2 = int(m21)+int(m22)+int(m23)
if(x1>=x2):
    print(name1)
else:
    print(name2)
