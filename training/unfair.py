arr=list(map(int,input().split(',')))
k=int(input())
mu=float('inf')
arr.sort()
minimum=[]

for i in range(len(arr)+1-k):
    subarray=arr[i:i+k]
    u=max(subarray)-min(subarray)
    if u<mu:
        mu=u
        minimum=subarray
        
print(' '.join(map(str,minimum)))
