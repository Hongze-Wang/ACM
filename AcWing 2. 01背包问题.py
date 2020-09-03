# AcWing 2. 01背包问题

# dp(i, j) 容量为j时前i个物品能取得的最大价值
# dp(i, j) = dp(i-1, j) 如果第i个物品不能装 (j < goods[i][0])
# dp(i, j) = dp(i-1, j-v_i) + w_i 能装 则容量减去第i物品的体积

n, v = map(int, input().split())
goods = []
for i in range(n):
    goods.append([int(i) for i in input().split()])

dp = [[0]*(v+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, v+1):
        dp[i][j] = dp[i-1][j] # if i < goods[i-1][0]
        if j >= goods[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-goods[i-1][0]] + goods[i-1][1])
            
print(dp[-1][-1])

# print(dp[-1][-1])

# 单数组解法 是在二维数组解法基础上改进而来的 是编程节省空间的思考
# 递推方程
# dp(j) = dp(j) 不装新的物品
# dp(j) = dp(j-v_i) + w_i 装新的物品i
# 但数组其实是从二维组优化而来的 因此并不是直接写出的递推方程
# 优化过程参见https://www.acwing.com/solution/content/3982/

n, v = map(int, input().split())
goods = []
for i in range(n):
    goods.append([int(i) for i in input().split()])

dp = [0] * (v+1)

for i in range(1, n+1):
    for j in range(v, -1, -1):   # j逆序因为我们希望dp[j-goods[i-1][0]] 保存上一轮的dp[j-goods[i-1][0]]如果是逆序的话 循环到当前位置它还没有被更新
        if j >= goods[i-1][0]:
            dp[j] = max(dp[j], dp[j-goods[i-1][0]] + goods[i-1][1])
print(dp[v])

# 优化内部循环边界条件

n, v = map(int, input().split())
goods = []
for i in range(n):
    goods.append([int(i) for i in input().split()])

dp = [0] * (v+1)

for i in range(1, n+1):
    for j in range(v, goods[i-1][0]-1, -1):
        dp[j] = max(dp[j], dp[j-goods[i-1][0]] + goods[i-1][1])
print(dp[v])
