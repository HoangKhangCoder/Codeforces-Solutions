from collections import Counter
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    unique =  sorted(list(set(nums)))
    cnts = Counter(nums)
    dp = [0] * len(unique)
    for i in range(len(unique) - 1, -1, -1):
        num = unique[i]
        if i == len(unique) - 1:
            dp[i] = num * cnts[num]
            continue
        if num + 1 != unique[i + 1]:
            dp[i] = num * cnts[num] + dp[i + 1]
            continue
        skip = dp[i + 1]
        if i == len(unique) - 2:
            choose = num * cnts[num]
        else:
            choose = num * cnts[num] + dp[i + 2]
        dp[i] = max(skip, choose)
    return dp[0]
print(solve())