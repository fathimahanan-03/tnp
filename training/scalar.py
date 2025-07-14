n=int(input())
v1=list(map(int,input().split()))
v2=list(map(int,input().split()))
sp=0
v1.sort()
v2.sort(reverse=True)

for i in range(len(v1)):
    sp+=v1[i]*v2[i]
    
print(sp)