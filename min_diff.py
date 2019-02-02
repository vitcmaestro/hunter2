n= int(input(""))
a = list(map(int,input().split()))
u,v = map(int,input().split())
x = a.index(u)
y = a.index(v)
if(x>y):
    print(x-y)
else:
    print(y-x)
