import math
def t1():
    class txl:
        name=''
        age=0
        phone=0
        email=''
        def __init__(self,n,a,p,e):
            self.name=n
            self.age=int(a)
            self.phone=int(p)
            self.email=e
        def out(self):
            print("name  %s\n年龄  %d\nphone %d\nemail %s"%(self.name,self.age,self.phone,self.email))
    ml={'qjx':[22,1777,4666]}
    while(1):
        x = int(input('选择操作:\n1查询 2录入 3删除\n'))
        if (x == 1):
            xx = input('name= ')
            a, p, e = ml[xx]
            print("年龄  %d\nphone %d\nemail %s" % (a, p, e))
        if (x == 2):
            #n, a, p, e = input("输入 姓名，年龄，电话，email\n")
            n = input("输入 姓名\n")
            a = int(input("输入 年龄\n"))
            p = int(input("输入 电话\n"))
            e = int(input("输入 email\n"))
            print(n,a,p,e)
            #ml.append([a,p,e])
            ml[n] = [a, p, e]
            print("ok",ml.items())
        if(x==3):
            print(ml.keys())
            d=input("要删除的人名\n")
            del ml[d]
            print('ok')
def t2(r):
    print("yc=%.3f"%(2*math.pi*r),"ys=%.3f"%(math.pi*r*r))
    print("qb=%.3f" % (4 * math.pi * r*r), "qt=%.3f" % (4/3*math.pi * (r**3)))
def t3(c):
    print('H=','%.1f'%(1.8*c+32))
def t4(l):
    f = open(r"D:\data.txt", "w")
    j = 1
    for i in range(0,l):
        o=str(j)
        f.write(o+"\n")
        j+=1
        if (j>100):
            j=1
        f.close
def t5():
    f=open(r"D:\input.txt","r")
    o=1
    while(1):
        s = f.readline()
        if s:
            print("di %d hang"%o,s)
        else:
            break
        o+=1
    f.close()


t1()
#t2(5)
#t3(37)
#t4(230)
#t5()