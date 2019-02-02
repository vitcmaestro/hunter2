n,k = map(int,input("").split())
a = list(map(int,input().split()))
for i in a:
    if(i == k):
        a.remove(i)
if(len(a) == 0):
    print("empty")
else:
    print(" ".join(map(str,a)))
