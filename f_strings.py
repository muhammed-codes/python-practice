name = "Ahmad"
coins = 3

message = "\n%s has %s coins left." %(name, coins)

message2 = "\n{1} has {0} coins left.".format(coins, name)

message3 = "\n{person} has {coins} coins left.".format(person=name, coins=coins)


player = {"player": "Muhammed", "balance": 5}
message4 = "\n{player} has {balance} coins left.".format(**player)

print(message)
print(message2)
print(message3)
print(message4)



print(f"\n{name} has {player["balance"]} coins left. We can even use fstrings to give him more coins, say {player["balance"] + 4} or {7 * 6}.")
