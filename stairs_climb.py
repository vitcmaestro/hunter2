n = int(input())
c = 0
for i in range(1,n):
    j = n-i
    if((i%2 == 0 or j%2 == 0) and i+j == n):
        c+=1
print(c)
