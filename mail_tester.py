import collections
test = input("")
d = True
freq = collections.Counter(test)
l = len(test)
if "@" in test and '.' in test:
    for x,y in freq.items():
        if(x== '@' and y!=1):
            print("NO")
            break
        elif(x == '.' and y!=1):
            print("No")
            break
    else:
        if(test.index('.') - test.index("@") <4):
            print("NO")
        elif(test.index("@") <3):
            print("NO")
        elif(test[l-4:l] != ".com"):
            print("NO")
elif("@" not in test or "." not in test):
    print("NO")
else:
    print("YES")
