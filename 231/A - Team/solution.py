n = int(input())
print(sum(1 for _ in range(n) if input().count("1") >= 2))