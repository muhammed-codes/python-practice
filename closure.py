#  closure is a func having access to the scope of its parent after the parent func has returned

def parent_func(person, coins = 3):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"\n{person} has {coins} coins left.")
        elif coins == 1:
            print(f"\n{person} has {coins} coin left.")
        else:
            print(f"\n{person} is out of coin.")
    return play_game

fatimah = parent_func("Fatimah")
azeezah = parent_func("Azeezah", 1)

fatimah()
fatimah()
azeezah()