s,n = map(str,input().split())
num = int(n)
res=""
for i in range(len(s)-num+1):
    res= res + s[i:i+num]+" "
print(res.strip())
