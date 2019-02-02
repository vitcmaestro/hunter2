n= int(input(""))
x = five=ten =z=y = 0
if(n>1000):
    x = n%1000
    n= n-(x*1000)
if(n>=500 and n<1000):
    five = 1
    n = n-500
if(n>=100 and n<500):
    y = n//100
    n = n-(y*100)
if(n>=50 and n<100):
    z = 1
    n = n-50
if(n>=10 and n<50):
    ten = n//10
    n = n -(ten*10)
print(x+five+y+z+ten+n)
