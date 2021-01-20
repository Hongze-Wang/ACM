# 01背包变形题
# 书店推出图书优惠活动，买书达到m原可获得赠品图书一本
# 求想要拿到赠品 需要花费的最少钱

# 请忽略解法1 解法2才是正确解法

# 解法1 需要排序
# m, n = map(int, input().split())
# book = list(map(int, input().split()))

# dp = [[9999] * (m+1) for _ in range(n+1)]

# book.sort(reverse=True)

# for i in range(n+1):
#     dp[i][0] = 0
# for i in range(m+1):
#     dp[0][i] = 0

# for i in range(1, n+1):
#     for j in range(book[i-1], m+1):
#         dp[i][book[i-1]] = book[i-1]

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if dp[i-1][j-1] >= j and dp[i-1][j-1] != 9999:
#             dp[i][j] = min(dp[i][j], dp[i-1][j-1])
#         if dp[i-1][j-1] + book[i-1] >= j and dp[i-1][j-1] != 9999:
#             dp[i][j] = min(dp[i][j], dp[i-1][j-1] + book[i-1])
#         if dp[i-1][j] + book[i-1] >= j and dp[i-1][j] != 9999:
#             dp[i][j] = min(dp[i][j], dp[i-1][j] + book[i-1])
#         if dp[i][j-1] + book[i-1] >= j and dp[i][j-1] != 9999:
#             dp[i][j] = min(dp[i][j], dp[i][j-1] + book[i-1])

# print(dp[n][m] if dp[n][m] < 9999 else -1)

# top-down dp
# dp(i, j) 购买前i本书中某些书到达金额j的最小花费
# 递推式
# if j >= book[i-1] 即当前需要达到的金额大于第i本书的价格
#     if dp(i-1, j) >= j 即前i-1本书做的选择已经达到j 则可以尝试购买第i本书看能否降低花费
#         dp(i, j) = min(dp(i-1, j), dp(i-1, j-book[i-1]) + book[i-1])
#     else               即前i-1本书做的选择没有达到j 则必须购买第i本书 在后续循环中的if分支找更优解
#         dp(i, j) = dp(i-1, j-book[i-1]+book[i-1])
# else 即当前所需要达到的金额小于第i本书的价格
#     if dp(i-1, j) >= j 即前i-1本书做的选择已经达到j 则可以尝试单独购买第i本书看能否降低花费
#         dp(i, j) = min(dp(i-1, j), book[i-1])
#     else 即前i-1本书做的选择没有达到j 则必须购买第i本书 在后续循环中的if分支找更优解
#         dp(i, j) = book[i-1]

# 递推式同时包含了对DP数组的初始化和针对子问题的优化


# 解法2 不需要排序 合并初始化过程到递推过程

m, n = map(int, input().split())
book = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(0, m+1):
        if j >= book[i-1]:
            if dp[i-1][j] >= j:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-book[i-1]] + book[i-1])
            else:
                dp[i][j] = dp[i-1][j-book[i-1]] + book[i-1]
        else: # j < book[i-1]
            if dp[i-1][j] >= j:
                dp[i][j] = min(dp[i-1][j], book[i-1])
            else:
                dp[i][j] = book[i-1]

print(dp[n][m] if dp[n][m] >= m else -1)
