n=input()
count=0
for i in n:
    if (i==i.upper()):
        count=count+1
if count>=1:
    print("Valid Password")
else:
    print("Invalid Password")