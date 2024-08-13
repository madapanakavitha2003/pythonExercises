n=input()
L=len(n)
count=0
for i in range(L):
    if (int(n[i])%2==0):
        count=count+1
if count>2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")