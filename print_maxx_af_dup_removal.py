n = input("")
dup = []
ans = []
for i in range(len(n)-1):
    x = list(n)
    if(n[i] == n[i+1] and n[i] not in dup):
        dup.append(n[i])
        del x[i]
        ans.append(x)
pri = max(ans)
print("".join(map(str,pri)))
