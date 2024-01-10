def count_coin_combinations(amount):
    coins = [1, 5, 10, 25]
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
    return dp[amount]
ways_to_make_30_cents = count_coin_combinations(30)
print(ways_to_make_30_cents)