n = int(input(""))
a = list(map(str,input().split()))
p = input("")
c = 0
for i in a:
    if(i.startswith(p)):
        c+=1
print(c)
