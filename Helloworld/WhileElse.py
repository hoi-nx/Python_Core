count=sum =0
print("Nhập danh sách các số dương dể tính ")

while count<5:
    val =float(input("Nhập số: "))
    if val<0:
        print("Sai quy tắc")
        break
    count+=1
    sum+=val
else:
    print("Điểm trung bình của bạn là= ", sum/count)