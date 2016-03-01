def give_change(amount):
    coins = [100, 50, 20, 10, 5, 2, 1]
    change = []
    for coin in coins:
        if coin <= amount:
            amount -= coin
            change.append(coin)
    return change


print give_change(645)
