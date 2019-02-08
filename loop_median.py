n = int(input(""))
a = list(map(int,input().split()))
mid = len(a)//2
if(n%2 !=0):
    print(a[mid])
    a.remove(a[mid])
    n-=1
while(len(a)!= 0 ):
    mid = len(a)//2
    avg = (a[mid]+a[mid-1])//2
    a.remove(a[mid])
    a.remove(a[mid-1])
    print(avg)
