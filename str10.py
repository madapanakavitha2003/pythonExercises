n=input()
a=""
for i in n:
    if i==i.upper():
        a=a+i.lower()
    else:
        a=a+i.upper()
print(a)