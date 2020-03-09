# RandomVectorWithFixedSum
Python implementation of the random vector with fixed sum.

Python的随机数很容易获得，只需调用numpy.random里的函数，常用的如

```python
numpy.random.rand(d0, d1, …, dn) # 产生均匀分布的随机数
numpy.random.randn(d0, d1, …, dn) # 产生标准正态分布随机数
numpy.random.randint(low[, high, size, dtype]) # 产生随机整数
```

该模块也可以产生具有分布的随机数，常用的如

```python
beta(a, b[, size]) # 贝塔分布
binomial(n, p[, size]) # 二项分布
chisquare(df[, size]) # 卡方分布
```

但如果想要具有约束的随机数，就比较困难。该仓库实现了带**和约束**的随机向量产生方法，并且向量的元素也是具有**范围约束**的，具体地说，即：

> 返回m个长度为n随机向量，每个随机向量元素的值在[a, b]范围内，并且每个随机向量元素的和为s；方法的返回值为大小为nxm的矩阵X，该矩阵满足numpy.sum(X, 0)=[s, s, s,...]。

具有范围约束的带和约束的随机向量产生方法在很多问题中会被用到，但是numpy并没有将其集成进来。本实现具有高效、快速的特点，算法复杂度低，本算法是基于MATLAB实现的改写。


