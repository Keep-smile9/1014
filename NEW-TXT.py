def o(e):
    for i in range(0, e):
        p = str(i)
        pp=p+'.txt'
        f = open(pp, "w")#'C:\Users\Lenovo\Desktop\'
        f.write("6666\n123!!\nsoso")
        f.close
def r():
    f=open(r"D:\222.txt","r")
    str = f.read()
    print(str)
    f.close


o(5)