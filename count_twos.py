def ispresent(i):
    x = str(i)
    if('2' in x):
        return True
    else:
        return False
def counter(i):
    coun = 0
    x = list(str(i))
    while('2' in x):
        x.remove('2')
        coun +=1
    return coun
n = int(input(""))
count = 0
for i in range(1,n+1):
    if(ispresent(i)):
        count+=counter(i)
print(count)
