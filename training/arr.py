import numpy as np

n=int(input())
arr=list(map(int,input().split()))
k=int(input())
j=0
count=0
distinct=set()
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if abs(arr[i]-arr[j])==k:
            pair=tuple(sorted((arr[i],arr[j])))
            distinct.add(pair)
            count+=1
            j+=1
print(distinct)
print(len(distinct))
        
        
    


