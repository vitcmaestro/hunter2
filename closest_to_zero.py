n = int(input(""))
a = list(map(int,input().split()))
miner = max(a)
for i in range(n):
    for j in range(i+1,n):
        rdiff = 0
        diff = a[i]+a[j]
        if(diff<0):
            while(diff<0):
                rdiff+=1
                diff+=1
        elif(diff>0):
            while(diff>0):
                rdiff+=1
                diff-=1
        else:
            rdiff = 0
        if(rdiff<miner):
            miner = rdiff
            x = a[i]
            y = a[j]
print(x,y)
