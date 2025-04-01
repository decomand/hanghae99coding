m,n=input().split()
m,n=int(m),int(n)

mans=list(range(n+1))
check=[True for x in range(n+1)]

for x in range(2,n):
    if check[x]==True:
        for u in range(x*x,n+1,x):
            check[u]=False

for x in range(m,n+1):
    if check[x]==True:
        print(x)

