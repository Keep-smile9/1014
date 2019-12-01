import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def cs1():
    s=pd.Series([1,4,'ww','aa'])
    print(s)
def cs2():
    s={'python':90,'c++':1,'c':2}
    print(s)
    s1=pd.Series(s)
    print(s1)

    print(s1.index)
    print(s1.values)

    s2=pd.Series(['a','b',123],index=['A',456,'C'])
    print(s2,s2['C'],s2[456])
def cs3():
    s3={"a":['a1','a2',78],"b":[564,855,'ui'],'c':[7,8,9]}
    out=pd.DataFrame(s3)
    print(out)
def cs4():
    s4=pd.date_range('20191024',periods=10)
    print(s4)
def cs5():
    print(pd.date_range('1/1/2000', periods=10))
    s5=pd.Series(np.random.rand(1000),index=pd.date_range('1/1/2000',periods=1000))
    s5=s5.cumsum()
    print(s5)
    s5.plot()
def cs6():
    s6 = pd.DataFrame(np.random.rand(1000,4), index=pd.date_range('1/1/2000', periods=1000),columns=['a','b','c'',d'])
    print(s6.cumsum())
    s6=s6.cumsum()
    plt.figure()
    s6.plot()
#cs1()
#cs2()
cs3()
#cs4()
#cs5()
#cs6()

