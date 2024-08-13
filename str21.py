n=input()
r=""
for x in n:
    if (x=="a") or (x=="e") or(x=="i")or(x=="o")or(x=="u")or(x=="A")or(x=="E")or(x=="I")or(x=="O")or(x=="U"):
        r=n.replace(x,"")
        n=r
print(r)