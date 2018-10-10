import sys
z=complex(2,3)
x='Xuân hội nguyễn'
print("thực= ",z.real)
print("ảo= ",z.imag)
print("type= ",type(z))

y=3**4
c=9/2

print("Thông tin chi tiết của kiểu int:= ",sys.int_info);
print("Thông tin chi tiết của kiểu float:= ",sys.float_info);
# hàm nhập từ bàn phím kiểu bool nếu người dùng nhập yes true t 1
def StrToBool(s):
    return s.lower() in ("yes","true","t","1")
print("Mời bạn nhập bool vào: ")
b=StrToBool(input())
# b=input("Mời bạn nhập true/false")
#xuất dấu * 15 lần không phải dùng for
print('*'*15)

try:
    x=4
    y=9
    z=x/y
except:
    print("")

t=51100
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60