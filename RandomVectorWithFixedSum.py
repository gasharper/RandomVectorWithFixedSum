import numpy as np

def RandomVectorWithFixedSum(n, m, s=1, a=0, b=1):
      """
          获得m个长度为n的随机向量
          随机向量元素的值在[a, b]范围内
          随机向量元素的和为s
          return 为[n, m]矩阵
                  np.sum(x, 0)为[1, 1, ..]
      """
      assert n*a<=s<=n*b and a<b
      n, m = int(n), int(m)
      s=(s - n*a) / (b - a)
      k = int(max(min(np.floor(s),n - 1),0))

      s1=s - np.arange(k, k-n, -1)
      s2=np.arange(k+n, k, -1) - s

      w=np.zeros((n,n + 1))
      w[0, 1]=np.inf

      t = np.zeros((n - 1,n))
      tiny = 1e-32

      for i in range(2, n+1):
          tmp1=w[i-2, 1:i+1] * s1[0:i] / i
          tmp2=w[i-2, 0:i] * s2[n-i: n] / i
          w[i-1, 1:i+1] = tmp1 + tmp2
          tmp3 = w[i-1, 1:i+1] + tiny
          tmp4 = (s2[n-i: n] > s1[0: i]).astype(np.float)
          t[i-2, 0:i] = (tmp2/tmp3)*tmp4 + (1-tmp1/tmp3)*(1-tmp4)

      x=np.zeros((n,m))
      if m == 0:
          return x

      rt=np.random.rand(n - 1,m)
      rs=np.random.rand(n - 1,m)

      s = s*np.ones((1, m)).astype(np.int)
      j = (k+1)*np.ones((1, m)).astype(np.int)
      sm=np.zeros((1,m))
      pr=np.ones((1,m))

      for i in range(n-1, 0, -1):
          e = rt[n-i-1, :] <= t[i-1, j-1]
          sx = rs[n-i-1, :]**(1/i)
          sm += (1-sx)*pr*s/(i+1)
          pr= sx*pr
          x[n-i-1, :] = sm + pr*e
          s = s - e
          j = j - e

      x[n-1, :] = sm + pr*s
      x = (b-a) * x + a
      return x
        
