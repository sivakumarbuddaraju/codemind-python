n=int(input())
a=n*n
d=(a-1)%9+1
if d==n:
    print("Neon Number")
else:
   print("Not Neon Number")