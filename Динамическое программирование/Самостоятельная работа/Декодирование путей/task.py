def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] in '0123456'):
            dp[i] += dp[i - 2]
    return dp[n]

print(num_decodings("11106"))
