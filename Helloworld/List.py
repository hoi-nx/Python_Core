lst=[]

list=[1,2,3,4,5,8,9,0,10]

list.sort(reverse=True) #giam dan

list[2] # tham chiếu đến phần tử thứ 2 của list 3

for x in list:
    print(x,end='\t')
print()

for i in range(len(list)):
    x=list[i]

#for ngược
for i in range(len(list)-1,-1,-1):
    x=list[i]

lst=[0]*10 #Khai báo list có 10 phần tử có giá tri mặc định là 0