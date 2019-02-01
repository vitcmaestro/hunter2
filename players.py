n = int(input())
play = list(map(int,input().split()))
j = 1
miner = sum(play)
ind = 0
while(j<n):
    x = sum(play[:j])
    y = sum(play[j:])
    if(x>y):
        res=x-y
    else:
        res=y-x
    if(res<miner):
       miner = res
       ind = n-j
       t1 = j
    j+=1
print(t1-ind)
