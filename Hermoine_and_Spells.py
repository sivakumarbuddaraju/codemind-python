a,b,c=map(int,input().split())
if c>b and b>a:
    print(c+b)
elif b>a and a>c:
    print(b+a)
else:
    print(a+c)