n,k = map(int,input("").split())
a = list(map(int,input().split()))
c = []
for i in a:
    if(i != k):
        c.append(i)
        
if(len(c) == 0):
    print("empty")
else:
    print(" ".join(map(str,c)))
