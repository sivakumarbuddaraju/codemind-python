n=int(input())
if n<=199:
    b=n*1.20
elif n>=200 and n<400:
    b=n*1.50
elif n>=400 and n<600:
    b=n*1.80
elif n>600:
    b=n*2.00
if n>400:
    b=b+b*0.15
    print("%.2f"%b)
else:
    b=b+100
    print("%.2f"%b)