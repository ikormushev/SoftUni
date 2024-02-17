def choose_coins(coins, target):
    coins_collected = {}
    total_coins_needed = 0

    coins.sort()

    while coins:
        current_coin = coins.pop()
        possible_coins = target // current_coin
        target %= current_coin

        if possible_coins > 0:
            coins_collected[current_coin] = possible_coins
            total_coins_needed += possible_coins

    string_to_print = ""
    if target != 0:
        string_to_print = "Error"
    else:
        string_to_print += f"Number of coins to take: {total_coins_needed}\n"

        for coin_value, total_coins in coins_collected.items():
            string_to_print += f"{total_coins} coin(s) with value {coin_value}\n"

    return string_to_print


given_coins = [int(x) for x in input().split(", ")]
target_sum = int(input())

print(choose_coins(given_coins, target_sum))
