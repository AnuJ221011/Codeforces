t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if k**2>n:
        print("NO")
    elif k % 2 != n % 2:
        print("NO")
    else:
        print("YES")