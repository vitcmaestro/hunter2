a = input("")
b = input("")
com = ""
for i in range(len(a)):
    for j in range(len(a),-1,-1):
        if(a[i:j] in b):
            if(len(a[i:j])>=len(com)):
                com = a[i:j]
print(com)
