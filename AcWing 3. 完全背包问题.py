# AcWing 3. 完全背包问题

n, v = map(int, input().split())
goods = []
# for i in range(n):
#     goods.append(list(map(int, input().split())))
for i in range(n):
    goods.append([int(x) for x in input().split()])

# 三循环解法 会超时 但是 却是所有解法的源泉
dp = [[0] * (v+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, v+1):
        k = 0
        while k*goods[i-1][0] <= j: # for(k=0; k*goods[i-1][0]<=j; k++) # 在容量不超的情况下 我可以选k个第i件物品
            dp[i][j] = max(dp[i][j], dp[i-1][j-k*goods[i-1][0]] + k*goods[i-1][1])

print(dp[-1][-1])


# 二维DP解法其实 是从三维DP优化过来的
# 记goods[i][0] = v_i goods[i][1] = w_i
# dp[i][j-v_i] = max(dp[i-1][j-v_i], dp[i-1][j-2*v_i] + w_i, dp[i-1][j-3*v_i] + 2*w_i, ...) (1)
# dp[i][j]     = max(dp[i-1][j],     dp[i-1][j-*v_i] + w_i,  dp[i-1][j-2*v_i] + 2*w_i, ...) (2)
# 逐项对比 发现式(1)能够代入式(2))
# dp[i][j]     = max(dp[i-1][j], dp[j][j-v_i]+w_i)
# 式(1)在第三重循环中求解 而式(2)在第二重循环中求解 因此第三重循环可以省去
# 某些DP问题下 第三重循环并不能省去 这是我把这个写在这里的原因 会解完全背包问题 不等于会解DP

dp = [[0] * (v+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, v+1):
        dp[i][j] = dp[i-1][j] # 初始化为不选第i个物品 不能像01背包那样 加j < good[i][0]的判断条件 原因写在注释a
        if j >= goods[i-1][0]:
            dp[i][j] = max(dp[i][j], dp[i][j-goods[i-1][0]] + goods[i-1][1])
print(dp[-1][-1])

# a
# 这里的dp(i-1, j)不是01背包的我不选第i个物品 而是可能是我前面选了几个第i件物品 仅在本次循环我不选了
# dp(i-1, j)保存了上次面对第i件我已经选择或者不选择第i件物品的价值 可能上一次循环还是能选的 即 j >= good[i][0]
# 但不能遗漏这个选择 动态规划 要考虑所有可能的选择 选最大的 不能像贪心那样只考虑贪心策略下的选择
# 这也是为什么动态规划 一定能找到最优解 而贪心不行

# 滚动数组优化
dp = [[0] * (v+1) for _ in range(2)]
for i in range(1, n+1):
    for j in range(1, v+1):
        dp[i&1][j] = dp[(i-1)&1][j]
        if j >= goods[i-1][0]:
            dp[i&1][j] = max(dp[i&1][j], dp[i&1][j-goods[i-1][0]] + goods[i-1][1])
print(dp[n&1][-1])
# 滚动数组优化说明了一个问题 每一个空间只需要两个位置就可以储存先前计算的结果 并不需要n个位置储存n的结果
# 这为进一步优化提供了条件

# 一维DP解法 是从二维优化过来的
dp = [0] * (v+1)
for i in range(1, n+1):
    for j in range(goods[i-1][0], v+1):
        dp[j] = max(dp[j], dp[j-goods[i-1][0]] + goods[i-1][1])

print(dp[-1])

# dp = [0] * (v+1)
# for i in range(n):
#     for j in range(goods[i][0], v+1):
#         dp[j] = max(dp[j], dp[j-goods[i][0]] + goods[i][1])

# print(dp[-1])
