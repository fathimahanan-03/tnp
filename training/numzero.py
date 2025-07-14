def countzero(n):
    result=0
    i=1
    while True:
        posVal,rem=divmod(n,i)
        prefix,posVal=divmod(posVal,10)
        if prefix==0:
            return result
        if posVal==0:
            result+=(prefix-1)*i+rem+1
        else:
            result+=prefix*i
        i*=10

n=int(input())        
print(countzero(n))

