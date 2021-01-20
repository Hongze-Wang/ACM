# 1409F - Subsequences of Length Two

# dp(i, j, k) 
# i: 第i个位置 j: 增加的子序列数目 k：余下的修改次数

def solve(i, j, k):
    if i >= n:
        return 0
    if dp[i][j][k] != -1:# memo法
        return dp[i][j][k]
    o = solve(i+1, j, k) # (1) 当前位置 不修改 最大子序列数目
    c = s[i] != t[0]     # 当前位置是否需要用t[0]修改
    if k >= c:           # 还有修改的机会
        o = max(o, solve(i+1, j+1, k-c)) # (2) 使用t[0]修改之后最大子序列数目
    c = s[i] != t[1]     # 当前位置是否需要用t[1]修改
    if k >= c:           # 还有修改的机会
        o = max(o, solve(i+1, j+(t[0] == t[1]), k-c) + j) # (3) 使用t[1]修改之后最大子数列数目
    dp[i][j][k] = o      # 贪心策略 这里o已经是三种情况最大值
    return o
 
n, k = map(int, input().split())
s = input()
t = input()
 
dp = [[[-1] * (n+1) for _ in [0]*n] for _ in [0]*n]
 
print(solve(0, 0, k))
