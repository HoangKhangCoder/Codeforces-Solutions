n = int(input())
bills = 0
for bill in [100, 20, 10, 5, 1]:
    bills += n // bill
    n %= bill
print(bills)