# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:51:51 2018

@author: yang
用于在spyder中测试numpy和pandas
当前python版本：Anaconda3.6
---------输入法！！！！！！！！！！！


"""
print('\n-----run->\n')
import pandas as pd
import numpy as np

a=pd.DataFrame([[0,1,2,3,4],[5,6,7,8,9]])
c=a.iloc[1,:]
print(c,c.idxmax())
#b=np.random.permutation(c.index)#[1 0]

print('\n>-done------|')