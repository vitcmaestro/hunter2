a = list(map(str,input().split()))
for i in range(len(a)):
    if(i%2 == 0):
        a[i] = a[i][::-1]
print(" ".join(map(str,a)))
