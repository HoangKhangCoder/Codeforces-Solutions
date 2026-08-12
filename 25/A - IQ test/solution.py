def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    cntOdds = sum(x % 2 for x in nums[:3])
    if cntOdds >= 2:
        rem = 0
    else:
        rem = 1
    for i, x in enumerate(nums):
        if x % 2 == rem:
            return i + 1
print(solve())