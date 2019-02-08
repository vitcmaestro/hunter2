a = input("")
a = a[::-1]
s = ""
for i in range(len(a)):
    if(a[i] not in s):
        s = s+a[i]
print(s)
