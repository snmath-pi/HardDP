n = int(input())
s = input()

cost = list(map(int, input().split()))

dp = [[[int(1e18) for _ in range(2)] for _ in range(2)] for _ in range(n)]

c = ord(s[0]) - ord('0')
dp[0][0][c] = 0; dp[0][0][c^1] = cost[0]
# print(dp)
for i in range(1, n):
    k = ord(s[i]) - ord('0')
    
    for j in range(2):
        dp[i][0][j] = dp[i-1][0][j^1] + (0 if k == j else cost[i])
        dp[i][1][j] = min(dp[i-1][0][j], dp[i-1][1][j^1]) + (0 if k == j else cost[i])

print(min(dp[n-1][1][0], dp[n-1][1][1]))

