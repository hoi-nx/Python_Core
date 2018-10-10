def handle(f,x):
    return f(x)
def soChan(x):
    return x%2==0;
ret1=handle(soChan,6)

ret2=handle(lambda x:soChan(x),6)