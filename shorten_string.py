n = input("")
n = n+" "
check = n[0]
s = ""
count = 1
for i in range(1,len(n)):
    if(n[i] == check):
        count+=1
    else:
        if(count == 1):
            s = s+n[i-1]
            check = n[i]
        else:
            s = s+str(count)+"*"+n[i-1]
            count = 1
            check = n[i]
           
print(s.strip())
