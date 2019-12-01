import numpy as np
def t1():
    a=np.empty(10)
    a[4]=1
    print(a)
def t2():
    a = np.random.randint(0,9,[5,3])#随机数0-9
    b = np.random.randint(0, 9, [3, 2])
    print(a,"\n\n",b,"\n\n",np.dot(a,b))
def t3():
    a = np.random.randint(0,90,10)
    print(a)
    for i in range(0,len(a)):
        min=a[i]
        p=i
        for n in range(i+1,len(a)):
            if(a[n]<min):
                min=a[n]
                p=n
        a[p]=a[i]
        a[i] = min
    print(a)
def t4():
    a=[1,2,0,0,4,0]
    b=[]
    for i in range(0,len(a)):
        if (a[i]==0):
            b.append(i)
    print(b)
def t5():
    a = np.random.randint(0, 90, [10, 10])
    print(a,"\n\nmax = ",np.max(a),"min = ",np.min(a))
def t6():
    a=np.matrix('3,3.2;3.5,3.5')
    print(a)
    b=np.matrix('118.4;135.2')
    a_n=np.linalg.inv(a)
    print(a_n)

    print(np.dot(a_n,b))
    print(a_n*b)
#t1()
#t2()
#t3()
#t4()
#t5()
t6()