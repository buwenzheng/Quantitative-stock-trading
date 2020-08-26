#!/usr/bin/env python
# -*- conding: UTF-8 -*-

# 在量化交易系统中数据分析是必不可少的步骤之一，提起Python环境下与数据分析相关的最重要的库一定非NumPy和Pandas莫属。
#
# Pandas则是Python环境下最有名、最专业的数据分析库，虽然NumPy提供了通用的数据处理的计算基础，但在处理表格数据时大多数使用者仍然将Pandas作为统计和分析工作的主要工具。Pandas使得Python中的处理数据变得非常方便、快速和简单。
#
# 可见Pandas是NumPy的升级，同时Pandas是围绕着 Series和 DataFrame两个核心数据结构展开的，但在量化交易系统开发中DataFrame数据结构的使用相对于Series更广泛。


# DateFrame 数据生成
# DataFrame是一个表格型的数据结构，既有行索引 index也有列索引columns，创建DataFrame的基本方法为df = pd.DataFrame(data, index=index,columns=columns)，其中data参数的数据类型可以支持由列表、一维ndarray或Series组成的字典、字典组成的字典、二维ndarray等。如下图所示，基本上可以把DataFrame看成是Excel的表格形态：


import pandas as pd

dd = pd.date_range('2010-01-01', freq='D', periods=1000)
print(dd, __name__)