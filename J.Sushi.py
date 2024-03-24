n = int(input())
c = list(map(int, input().split()))

dp = [[[0.0 for _ in range (310)] for _ in range(310)] for _ in range(310)]

cnt = [0] * (4)

for val in c:
    cnt[val]+=1

for three in range(0, 310):
    for two in range(0, 310):
        for one in range(0, 310):
            zero = n - two - three - one
            if zero == n:
                continue
            if one + two + three > n: 
                continue
            tot = 1
            if three >= 1:
                tot += three / n * dp[three-1][two + 1][one]
            if two >= 1:
                tot += two / n * dp[three][two-1][one+1]
            if one >= 1:
                tot += one / n * dp[three][two][one-1]
            dp[three][two][one] = tot / (1 - zero / n)

print(dp[cnt[3]][cnt[2]][cnt[1]])
        
                
