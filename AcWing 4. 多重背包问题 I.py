# AcWing 4.多重背包问题
# 转换成01背包来解

import sys

n, m = map(int, input().split())
lines = sys.stdin.readlines()
v = [0]
w = [0]
n = 0
for line in lines:
    line = list(map(int, line.split()))
    v.extend([line[0]] * line[2])
    w.extend([line[1]] * line[2])
    n += line[2]

class Solution:
    def get_max_value(self, n, m, v, w):
        dp = [0] * (m+1)
        for i in range(1, n+1):
            for j in range(m, v[i]-1, -1):
                dp[j] = max(dp[j], dp[j-v[i]]+w[i])
        return dp[m]

print(Solution().get_max_value(n, m, v, w))
