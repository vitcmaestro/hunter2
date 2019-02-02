n,d = map(int,input().split())
a = list(map(str,input().split()))
for i in range(d):
    c = a[0]
    a.remove(a[0])
    a.append(c)
print(" ".join(map(str,a)))
    
