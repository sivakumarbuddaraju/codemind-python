n=int(input())
print(f"Units Consumed: {n}")
if n<=199:
    c=1.20
    print("Cost per Unit: 1.20")
elif n>=200 and n<400:
    c=1.40
    print("Cost per Unit: 1.40")
elif n>=400 and n<600:
    c=1.60
    print("Cost per Unit: 1.60")
elif n>=600 and n<800:
    c=1.80
    print("Cost per Unit: 1.80")
elif n>=800:
    c=2.00
    print("Cost per Unit: 2.00")
b=n*c
print(f"Bill: {b:.2f}")
if b>400:
    s=b*0.15
    print(f"Surcharge: {s:.2f}")
    t=b+s
    print(f"Total Amount: {t:.2f}")
else:
    print(f"Surcharge: 0.00")
    t=b
    print(f"Total Amount: {t:.2f}")