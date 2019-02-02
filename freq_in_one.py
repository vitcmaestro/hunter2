import collections
n = int(input(""))
a = list(map(int,input().split()))
freq = dict(collections.Counter(a))
for x,y in freq.items():
    if(y==1):
        print(x)
