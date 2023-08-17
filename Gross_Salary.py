n=int(input())
if n<=10000:
    d=(n*80)/100
    h=(n*20)/100
    gs=n+d+h
    print("%.2f"%gs)
elif n<=20000:
    d=(n*90)/100
    h=(n*25)/100
    gs=n+d+h
    print("%.2f"%gs)
elif n>20000:
    d=(n*95)/100
    h=(n*30)/100
    gs=n+d+h
    print("%.2f"%gs)