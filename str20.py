n=int(input())
for i in range(n,0,-1):
    spaces=(n-i)*"  "
    print(spaces+("* "*i))