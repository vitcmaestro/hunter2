n= int(input(""))
a = list(map(int,input().split()))
c =[]
for i in range(n-1):
    x = max(a[i+1:])
    c.append(str(x))
c.append(str(0))
print(" ".join(map(str,c)))
