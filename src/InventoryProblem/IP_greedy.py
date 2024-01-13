from model.Shoe import *
import time


def IP_start_greedy(shoe_list):
    print("Greedy started")
    time_start = time.time()
    shop1, shop2, difference, sum_shop1, sum_shop2 = solve_greedy(shoe_list)
    time_end = time.time()
    print(f"\n🏪  Store 1 Inventory (💵 Total price: {sum_shop1}€):")
    for shoe in shop1:
        print(f" 👟",shoe.name)
    print(f"\n🏪  Store 2 Inventory (💵 Total price: {sum_shop2}€):")
    for shoe in shop2:
        print(f" 👟",shoe.name)
    print(f"\n🏪  Store 1 💵 Total price: {sum_shop1}€:")
    print(f"\n🏪  Store 2 💵 Total price: {sum_shop2}€:")
    print(f"\n💰  Best price difference: €{difference}\n")
    print("Greedy ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")


def solve_greedy(shoe_list):
    shoe_list.sort(key=lambda x: x.price, reverse=True)

    shop1 = []
    shop2 = []

    sum_shop1 = 0
    sum_shop2 = 0

    # My initial solution was to put even shoes on one shop and odd shoes on the other
    # This solution is better because it balances out the prices a little bit better
    for shoe in shoe_list:
        if sum_shop1 <= sum_shop2:
            shop1.append(shoe)
            sum_shop1 += shoe.price
        else:
            shop2.append(shoe)
            sum_shop2 += shoe.price

    difference = abs(sum_shop1 - sum_shop2)
    return shop1, shop2, difference, sum_shop1, sum_shop2
