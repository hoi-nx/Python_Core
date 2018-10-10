#Round làm tròn
from random import randrange
from math import *
from time import clock

a=3
b=11
c=b/a
print(c)
print("Làm tròn ",round(c))

#time
#start =clock()
print("Mời bạn nhập một giá trị: ")
x=input()
print("Bạn nhập x,",x)
#end=clock()
#duration=end-start;
#print("",duration)

#Random
count =0;
randrange(-100,100) # chạy ngẫu nhiên từ -100 đến 99
while True:
    x=randrange(-100,100)
    count+=1;
    print(x, end=',')
    if x is 50:
        break
print("#"*30)
# exit() tắt phần mềm
# Eval tính toán chuỗi phép toán
g=eval("5+7-9+sin(30)")
print(g)

#Nhập nhiều biến từ bàn phím vd nhập 5,6 thì nó hiểu x1=5 x2=6
x1,x2 =eval(input("Nhập x1,x2"))
print("x1= ",x1," x2= ",x2)