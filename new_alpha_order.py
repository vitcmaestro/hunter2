z = list(map(str,input().split()))
n = int(z[0])
d = 0
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lis = []
for i in range(1,n+1):
    x = z[i][0]
    if(x not in lis):
        lis.append(x)
        d= 0
    else:
        print("impossible")
        d = 1
        break
if(d == 0):
    for i in range(1,n):
        if(ord(lis[i-1])>ord(lis[i])):
            x = a.index(lis[i])
            y = a.index(lis[i-1])
            del a[x]
            a.insert(y,lis[i])
    print("".join(map(str,a)))
