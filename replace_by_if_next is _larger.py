n = int(input(""))
a = list(map(int,input().split()))
for i in range(n-1):
    if(a[i+1]<a[i]):
        a[i] = a[i+1]
    else:
        a[i] = -1
a.remove(a[n-1])
a.append(-1)
print(" ".join(map(str,a)))
