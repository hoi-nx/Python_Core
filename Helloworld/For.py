#range(begin,end,step) step bước nhẩy

range(10)
range(1,10)
range(1,10,2)

range(10,0,-1) #for ngược

n=10
s=0
if n%2==0:
    for x in range(2,n+1,2):
        s=s+x
else:
    for x in range(1,n+1,2):
        s=s+x
print("Tổng s= ",s)
