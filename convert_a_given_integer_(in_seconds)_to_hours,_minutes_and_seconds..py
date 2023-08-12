n=int(input())
h=n/3600
m=(n%3600)/60
s=n%60
print(f"H:M:S-{int(h)}:{int(m)}:{int(s)}")