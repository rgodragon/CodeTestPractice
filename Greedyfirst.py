n = 3760
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin #몫
    n = n % coin #나머지

print(count)