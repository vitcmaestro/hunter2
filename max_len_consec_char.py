a = input("")
maxer = 0
check = a[0]
count = 1
ans = check
for i in range(1,len(a)):
    if(a[i] == check):
        count+=1
        if(count > maxer):
            maxer = count
            ans = a[i]
    else:
        count = 1
        check = a[i]
    
print(ans,maxer)
