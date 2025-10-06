def lrs(s):
    n = len(s)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i, j = n, n
    res = ""
    while i > 0 and j > 0:
        if s[i-1] == s[j-1] and i != j:
            res = s[i-1] + res
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    print("Longest Repeating Subsequence:", res)

s = "AABCBDC"
lrs(s)
