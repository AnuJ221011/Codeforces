t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    count=0
    for i in range(n):
        if s[i]=='1':
            count+=1
    if count==0:
        print("YES")
    elif count==2:
        for i in range(1,n):
            if s[i]=='1' and s[i-1]=='1':
                print("NO")
                break
        print("YES")
    elif count%2==0:
        print("YES")
    elif count%2==1:
        print("NO")