n= int(input(""))
a = list(map(int,input().split()))
u,v = map(int,input().split())
x =[index for index, value in enumerate(a) if value == u]
y = [index for index, value in enumerate(a) if value == v]
miner = n
for i in range(len(x)):
    for j in range(len(y)):
        if(x[i]>y[j]):
            diff = x[i]-y[j]
        else:
            diff = y[j]-x[i]
        if(diff<miner):
            miner = diff
print(miner)
