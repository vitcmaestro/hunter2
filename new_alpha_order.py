n = int(input(""))
z = list(map(str,input().split()))
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lis = []
for i in range(n):
    x = z[i][0]
    if(x not in lis):
        lis.append(x)
for i in range(1,n):
    if(ord(lis[i-1])>ord(lis[i])):
        x = a.index(lis[i])
        y = a.index(lis[i-1])
        del a[x]
        a.insert(y,lis[i])
print("".join(str,a))
