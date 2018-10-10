n=int(input("Nhập chiều cào: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==j or j==n-1:
            print("x",end='') # end='' nối đuôi trên cùng 1 dòng
        else:
            print(" ",end='')
    print() #kết thúc 1 dòng thì xuống dòng
print("#"*30)
i=0
while i<n:
    j=0
    while j<n:
        if j is 0 or i is j or j is n-1:
            print("#",end='')
        else:
            print(" ",end='')
        j+=1
    i+=1
    print()

for i in range(1,11):
    for j in range(2,10):
        line= "{0}*{1:>2}={2:>2}".format(j,i,i*j)
        print(line,end='\t\t')
    print()