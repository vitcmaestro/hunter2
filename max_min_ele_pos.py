n = int(input())
a = list(map(int,input().split()))
x = a.index(max(a))
y = a.index(min(a))
print(y+1,x+1)
