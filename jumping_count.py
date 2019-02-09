def isjumping(x):
    lis = list(str(x))
    c = 0
    if(len(lis) == 1):
        return True
    else:
        for i in range(len(lis)-1):
            z = int(lis[i])
            y = int(lis[i+1])
            if(z-y == 1 or y-z == 1):
                c+=1
        if(c == len(lis)-1):
            return True
        else:
            return False
n=int(input(""))
count = 0
for i in range(n):
    if(isjumping(i)):
        count+=1
print(count)
