n = int(input())
play = list(map(int,input().split()))
i = 0
j = n-1
team1 = 0
team2 = 0
res = max(play)
x= -1
y = -1
oneplay = 0
twoplay = 0
while(i<j):
    if(i != x):
        team1+=play[i]
        x = i
    else:
        pass
    if(j!=y):
        team2+=play[j]
        y = j
    if(team1>team2):
        diff = team1 - team2
        twoplay+=1
        j-=1
    elif(team2>team1):
        diff = team2-team1
        oneplay+=1
        i+=1
    if(diff<res):
        res = diff
    print(oneplay,twoplay)
if(oneplay>=twoplay):
    print(oneplay-twoplay)
else:
    print(twoplay-twoplay)
