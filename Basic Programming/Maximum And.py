T=int(input())
for _ in range(T):
    A,B=map(int,input().split())
    if (B==A+1):
        print(A&B)
    else:
        print(max(B&(B-1),(B-1)&(B-2)))
