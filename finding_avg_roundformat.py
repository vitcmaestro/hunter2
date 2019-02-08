n = int(input(""))
x = 0
for i in range(n):
    temp = list(map(int,input().split()))
    x = x+ sum(temp)
count = n*n
ans = x/count
print("{0:.6f}".format(round(ans,6)))
