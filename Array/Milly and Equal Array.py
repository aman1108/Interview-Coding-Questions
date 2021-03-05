import sys
input=sys.stdin.readline
import math
for _ in range(int(input())):
    N,X,Y,Z=map(int,input().split())
    A=list(map(int,input().split()))
    val=A[0]

    flag=0
    for i in range(N):
        res=A[i]
        while(res%X==0):
            res=res//X
        while(res%Y==0):
            res=res//Y
        while(res%Z==0):
            res=res//Z
        A[i]=res
        if (i!=0 and A[i]!=A[i-1]):
            flag=1
            break
        
    if (flag==0):
        print("She can")
    else:
        print("She can't")
