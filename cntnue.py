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
n = len(ins)
for i in range(5):
    for j in range(5):
        if(a[i][j] == ins[0]):
            for x in range(i,i+len(ins)):
                if(x<=5 and a[x][j] == ins[x]):
                    z+=1
            if(z == len(ins)-1):
                res = str(i)+" "+str(j)+" "+str(x)+" "+str(j)
            for x in range(j,j+len(ins)):
                if(j<=5 and a[i][x] == ins[x]):
                    v+=1
            if(v == len(ins)-1):
                res = str(i)+" "+str(j)+" "+str(i)+" "+str(x)
            for x in range(1,len(ins)):
                if(a[i][n-x] == ins[x]):
                    w+=1
            if(w == len(ins)-1):
                res = str(i)+" "+str(j)+" "+str(i)+" "+str(x)
print(res)
                    
