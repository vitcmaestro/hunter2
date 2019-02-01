n = int(input())
play = list(map(int,input().split()))
lucky = 0
for i in range(n):
    x = (n*(i+1))
    if(x in play):
        lucky = play[i]
        break
print(lucky)
