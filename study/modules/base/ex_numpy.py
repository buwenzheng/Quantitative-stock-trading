# import name 引入模块
# from…import Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
# from modname import name1[, name2[, ... nameN]]
# form import * 导入一个模块中所有的项目


import random
import matplotlib.pyplot as plt
import numpy as np
from timeit import timeit

# walk = []
# for _ in range(1000):
#     walk.append(random.normalvariate(0,1))
# print('walk', walk)
#
# plt.hist(walk, bins=30)
# plt.show()

# plt.hist(np.random.normal(loc=0.0, scale=1.0, size=1000), bins=30)
# plt.show()

def list_test():
    walk = []
    for _ in range(100000):
        walk.append(random.normalvariate(0,1))

def ndarray_test():
    np.random.normal(loc=0.0, scale=1.0, size=100000)
# numpy.ndarray 为numpy的核心，不仅具有矢量算术运算的能力，并且在处理多维的大规模数组时快速且节省空间
# 运行时间测试
# t1 = timeit('list_test()', 'from __main__ import list_test', number=1)
# t2 = timeit('ndarray_test()', 'from __main__ import ndarray_test', number=1)
#
# print('list: {}'.format(t1))
# print('ndarray: {}'.format(t2))

stock_data = np.random.normal(loc=10, scale=1.0, size=1000)
stock_data = np.around(stock_data, 2)

# print('stock_data: \n {}'.format(stock_data))
pct_change = np.around((stock_data - np.roll(stock_data, 1))/np.roll(stock_data,1), 2)
pct_change[0] = np.nan
print('pct_change: \n {}'.format(pct_change))

plt.hist(pct_change, bins=30)
plt.show()