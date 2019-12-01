import numpy as np
def t4():
    while (1):
        x = input('in ')
        y = 0
        print(len(x))
        for i in range(0, len(x)):
            y += 1
        print(y)
def t5():
    i=1
    o=0
    while(i<=99):
        i+=1
        o+=i
        print(o,i)
def t6():
    while(1):
        x = int(input('in'))
        if ((x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))):
            print('yes')
        else:
            print('no')
def t7():
    i=9
    o=1
    p=1
    while(i):
        i-=1
        print('*' * o)
        if(o==5):
            p=2
        if (p==1):
            o+=1
        else:
            o-=1
def t8():
    o=[0,1]
    o[0]=input('a')
    o[1]=input('b')
    s=sorted(o)
    print(s[0],s[1],s[:],o)
def t10():
    for i in range(0,100):
        for o in range(0,i):
            if((i**2)-(o**2)==168):
                print((o**2)-100)
def t11():
    for i in range(1,15):
        o=17*i
        if(o>200):
            break
    print(i - 1)
def t12():
    n=int(input('n='))
    c=[2,3,5,7,11,13,17,19,23,27,29]
    for i in range(0,len(c)):
        if(n%c[i]==0):
            p=1
def t13():
    x=c=100
    o=10
    for i in range(0,o):
        x=x/2
        c+=x
    print(c,x)
def t14():
    a=np.arange(100,201)
    #print(a)
    b=[]
    for i in range(0,101):
        l=0
        for p in range(1,20):
            if(a[i]%p==0):
                l=l+1
        if (l == 2):
            b.append(a[i])


    print(b)

def t15():
    d={'a':1,'b':2,'c':3}
    print(d.keys(),d.values())
#t4()
#t5()
#t6()
#t7()
#t8()
#t10()
#t11()
#t12()
#t13()
t14()
#t15()