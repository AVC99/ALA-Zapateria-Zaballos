from model.Shoe import *
from itertools import combinations
import time


def IP_start_bruteforce(shoe_list):
    print("Brute force started")
    time_start = time.time()

    # Number of shoes in the list
    n = len(shoe_list)

    # Initialize the best (minimum) price difference and the corresponding partitions
    best_difference = float("inf")
    best_part1 = []
    best_part2 = []

    # Iterate through all possible combinations
    for i in range(n + 1):
        # Generating combinations of shoes for one part of the inventory
        combinations_list = combinations(shoe_list, i)
        for combination in combinations_list:
            part1 = list(combination)
            part2 = [s for s in shoe_list if s not in part1]

            # Calculate the total price for each part
            price_part1 = sum(s.price for s in part1)
            price_part2 = sum(s.price for s in part2)

            # Calculate the price difference between the two parts
            difference = abs(price_part1 - price_part2)

            # Update the best partition if a new minimum difference is found
            if difference < best_difference:
                best_difference = difference
                best_part1 = part1
                best_part2 = part2

    time_end = time.time()

    # Display the results
    print("\n-------------------------------")
    print("Inventory division using brute force")
    print("-------------------------------")
    print(f"💰  Best price difference: €{best_difference:.2f}")

    total_price_part1 = sum(s.price for s in best_part1)
    print("\n🏪  Store 1 Inventory (💵 Total price: {:.2f}€):".format(total_price_part1))
    for s in best_part1:
        print(f"   👟  {s.name} - €{s.price}")

    total_price_part2 = sum(s.price for s in best_part2)
    print("\n🏪  Store 2 Inventory (💵 Total price: {:.2f}€):".format(total_price_part2))
    for s in best_part2:
        print(f"   👟  {s.name} - €{s.price}")

    print("\n-------------------------------")
    print("Brute force ended")
    print("Time elapsed: {:.5f} seconds".format(time_end - time_start))
