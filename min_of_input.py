n = int(input(""))
a = list(map(int,input().split()))
miner = a[0]
res=""
for i in a:
    if(i<= miner):
        miner = i
    res=res+str(miner)+" "
print(res.strip())
