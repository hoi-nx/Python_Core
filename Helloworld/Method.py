def add(x,y):
    return x+y

def tinh(a,b):
    if(a is 0 and b is 0):
        return "Phương trình vô số nghiệm"
        print("Phương trình vô so nghiệm")
    elif a is 0 and b is not 0:
        print("Vô nghiêm")
    else:
        print("Nghiêm x={0}:".format(round(-b/a)))


def SumRange(n,m=0):
    sum=0
    for i in range(1,m+n,1):
        sum=i
    return sum