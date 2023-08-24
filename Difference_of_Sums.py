n=int(input())
a=(n*(n+1)//2)**2
s=0
for i in range(1,n+1):
    s+=i**2
print(abs(a-s))