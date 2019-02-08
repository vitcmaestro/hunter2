a = list(map(str,input().split()))
i = len(a)-1
if(a[len(a)-1][len(a[i])-1] == '.'):
    a[i] = a[i][:len(a[i])-1]
for i in range(len(a)):
    if(i%2 == 0):
        a[i] = a[i][::-1]
print(" ".join(map(str,a)))
