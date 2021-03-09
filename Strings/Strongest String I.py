n=int(input())
s=list(input())
ans=[max(s)]
ind=s.index(ans[0])
for i in range(ord(ans[0])-1,96,-1):
    #print(ind,chr(i))
    try:
        ind=ind+s[ind+1:].index(chr(i))+1
        ans.append(chr(i))
    except:
        continue
        
        

print(*ans,sep="")
    
