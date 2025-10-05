from collections import defaultdict

def find_coins_greedy(change: int, coins: list) -> dict:
    coins_used = defaultdict(int)
    
    for coin in coins:
        if change == 0:
            break
        
        count = change // coin
        if count > 0:
            coins_used[coin] = count
            change -= coin * count
    
    return dict(coins_used)

def find_min_coins(change: int, coins: list) -> dict:
    # dp[i] = the minimum number of coins needed to make the amount i
    dp = [0] + [float("inf")] * change
    last_coin = [0] * (change + 1)

    for amount in range(1, change + 1):
        for coin in coins:
            if amount >= coin and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
                last_coin[amount] = coin

    coins_used = defaultdict(int)
    current_change = change
    while current_change > 0:
        coin = last_coin[current_change]
        coins_used[coin] += 1
        current_change -= coin

    return dict(coins_used)

def main():
    coins = [50, 25, 10, 5, 2, 1]
    change = 113
    print(f"Result of the greedy algorithm for change = {change}: {find_coins_greedy(change, coins)}")
    print(f"Result of the DP algorithm for change = {change}: {find_min_coins(change, coins)}")

if __name__ == "__main__":
    main()
