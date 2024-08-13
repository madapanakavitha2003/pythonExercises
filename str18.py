n=input()
n1=""
for i in range(1,len(n)):
    if n[i]==n[i].upper():
        n1=n1+"-"+n[i].lower()
    else:
        n1=n1+n[i]
print(n[0].lower()+n1)