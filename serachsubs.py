s = "WELCOMETOGUVICORPORATIONS"
j =0
a=[]
z = 0
v = 0
w = 0
u = 0
res=""
for i in range(5):
    temp = s[j:j+5]
    j+=5
    a.append(temp)
ins = input("")
print(a)
n = len(ins)
for i in range(5):
    for j in range(5):
        if(a[i][j] == ins[0]):
            x = 1
            while(x+i<=4 and x<n):
                if(a[x+i][j] == ins[x]):
                    z+=1
                x+=1
                if(z == n-1):
                    res = str(i)+" "+str(j)+"\n"+str(x+i-1)+" "+str(j)
                    print(res)
                    break
            if(z!=(n-1)):
                y = 1
                while(y+j<=4 and y<n):
                    if(a[i][y+j] == ins[y]):
                        v+=1
                    y+=1
                if(v == n-1):
                    res = str(i)+" "+str(j)+"\n"+str(i)+" "+str(x+j-1)
                    print(res)
                    break
            if(v!=(n-1)):
                l= 1
                while(i-l >=0 and l<n):
                    if(a[i-l][j] == ins[l]):
                        w+=1
                    l+=1
                if(w == (n-1)):
                    res = str(i)+" "+str(j)+"\n"+str(l-i+1)+" "+str(j)
                    print(res)
                    break
            if(u!=(n-1)):
                l= 1
                while(j-l >=0 and l<n):
                    if(a[i][j-l] == ins[l]):
                        u+=1
                    l+=1
                if(u == (n-1)):
                    res = str(i)+" "+str(j)+"\n"+str(i)+" "+str(j-l+1)
                    print(res)
                    break
if(res == ""):
    print(0)
