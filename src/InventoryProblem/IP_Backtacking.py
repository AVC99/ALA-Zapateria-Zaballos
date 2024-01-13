from model.Shoe import *
import time


def IP_start_backtracking(shoe_list):
    def backtrack(index, part1, part2):
        nonlocal best_difference, best_part1, best_part2

        if index == len(shoe_list):
            # Calculate the price difference and update the best solution
            difference = abs(sum(s.price for s in part1) - sum(s.price for s in part2))
            if difference < best_difference:
                best_difference = difference
                best_part1 = part1.copy()
                best_part2 = part2.copy()

        else:
            # Include the shoe in the first part and explore
            part1.append(shoe_list[index])
            backtrack(index + 1, part1, part2)
            part1.pop()  # Go back

            # Include the shoe in the second part and explore
            part2.append(shoe_list[index])
            backtrack(index + 1, part1, part2)
            part2.pop()  # Go back

    print("Backtracking started")
    time_start = time.time()

    best_difference = float("inf")
    best_part1 = []
    best_part2 = []

    # Start the recursion from index 0
    backtrack(0, [], [])

    time_end = time.time()
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
    print("Backtracking ended")
    print(f"Execution Time: {time_end - time_start} seconds")

    return best_part1, best_part2
