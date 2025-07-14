n,d=map(int,input().split())
j=list(map(int,input().split()))

j.sort(reverse=True)

jam=sum(j[:d])
print(jam)
    
    