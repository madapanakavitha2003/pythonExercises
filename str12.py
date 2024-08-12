n=input()
a=0
b=0
c=0
for i in n:
    if (i==i.isdigit()):
        a=a+1
    elif i==i.upper():
        b=b+1
    elif i==i.lower():
        c=c+1
if a>=1 and b>=1 and c>=1:
    print("Valid Password")
else:
    print("Invalid Password")