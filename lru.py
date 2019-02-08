n,k = map(int,input().split())
a = list(map(int,input().split()))
cache = [0]*k
freq = []
if(n<=k):
    print(" ".join(map(str,a)))
else:
    for i in range(k):
        cache[i] = a[i]
        freq.append(i)
    for i in range(k+1,n):
        if(a[i] in cache):
            freq.remove(cache.index(a[i]))
            freq.append(cache.index(a[i]))
        else:
            cache.remove(cache[freq[0]])
            cache.insert(freq[0],a[i])
            freq.append(freq[0])
            freq.remove(freq[0])
    print(" ".join(map(str,cache)))
