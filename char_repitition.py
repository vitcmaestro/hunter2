s = input()
i = 0
res=""
while(i<len(s)):
    if(ord(s[i])>=97 and ord(s[i])<=122):
        alpha = s[i]
        i+=1
        temp= s[i]
        num =""
        while(i<len(s) and ord(s[i])>=48 and ord(s[i])<=57):
            num =num+s[i]
            i+=1
        n = int(num)
        if(n%2 == 0):
            for j in range(n):
                res=res+alpha
        else:
            res=res+alpha+num
print(res)
