# 01背包变形题
# 书店推出图书优惠活动，买书达到m原可获得赠品图书一本
# 求想要拿到赠品 需要花费的最少钱


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