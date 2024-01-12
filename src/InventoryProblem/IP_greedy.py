from model.Shoe import *


def IP_start_greedy(shoe_list):
    shop1, shop2, difference = solve_greedy(shoe_list)

    print("Shop 1:")
    for shoe in shop1:
        print(shoe.name)
    print("Shop 2:")
    for shoe in shop2:
        print(shoe.name)
    print("Difference: ", difference)

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
    return shop1, shop2, difference
