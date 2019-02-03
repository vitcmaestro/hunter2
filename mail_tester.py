import collections
test = input("")
d = True
freq = collections.Counter(test)
l = len(test)
if "@" in test and '.' in test:
    diff = test.index('.') - test.index("@")
    for x,y in freq.items():
        if(x== '@' and y!=1):
            print("NO")
            break
        elif(x == '.' and y!=1):
            print("No")
            break
    else:
        if(diff <4 and diff >5):
            print("NO")
        elif(test.index("@") <3):
            print("NO")
        elif(test[l-4:l] != ".com"):
            print("NO")
        else:
            print("YES")
elif("@" not in test or "." not in test):
    print("NO")

