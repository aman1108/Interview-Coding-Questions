
A=list(map(int,input().split()))
#A = [ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 ]
N=len(A)

G=[]
v=max(A)
a=len(str(v))+1

for j in range(N):
    v=str(A[j])*a
    G.append([v[:a],A[j]])

G.sort(reverse=True)

#print(G)
s=""
for j in G:
    s=s+str(j[1])
print(s)
