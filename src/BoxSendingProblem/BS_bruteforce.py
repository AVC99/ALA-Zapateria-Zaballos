from model.Shoe import *
from model.Box import *
import time
import copy


def BS_start_bruteforce(shoe_list):
    print("Bruteforce started")
    time_start = time.time()
    box_counter = 0
    # Generate all possible combinations of boxes for each shoe
    all_combinations = generate_shoe_combinations(shoe_list)

    #print_combinations(all_combinations)

    recalculate_price(all_combinations)
    print("Recalculated prices")
    #print_combinations(all_combinations)
    
    # Find the best solution
    best_price, best_combination = find_best_solution(all_combinations)

    print_best_combination(best_combination)

    time_end = time.time()
    print("Bruteforce ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")
    print("Box counter: " + str(box_counter))


def print_best_combination(best_combination):
    print("Best solution:")
    for j, box in enumerate(best_combination, 1):
        print(f"Box {j} contains:")
        for shoe in box.shoes:
            print(shoe.name)
        print(f"Price: {box.price}")

def find_best_solution(all_combinations):
    best_price = float("inf")
    best_combination = []

    for i, combinations in enumerate(all_combinations, 1):
        print(f"SOLUTION : {i}:")
        combination_price = 0
        for j, box in enumerate(combinations, 1):
            print(f"Box {j} price: {box.price}")
            if box.price >= 1000:
                print("Box price is too high")
                combination_price = float("inf")
                break  # skip this box but continue with the next box
            elif combination_price + box.price >= best_price:
                print("Combination price is too high")
                combination_price = float("inf")
                break
            else:
                combination_price += box.price
                print(f"Combination price: {combination_price}")

        # if the total price of this combination is higher than the best price found so far
        if combination_price < best_price:
            print(f"NEW BEST PRICEEEEE : {combination_price}")
            best_price = copy.deepcopy(combination_price)
            best_combination = copy.deepcopy(combinations)

    return best_price, best_combination

def recalculate_price(all_combinations):
    for i, combinations in enumerate(all_combinations, 1):
        for j, box in enumerate(combinations, 1):
            box.calculate_price()
            print(f"Box {j} price: {box.price}")


def generate_shoe_combinations(shoe_list):
    all_combinations = []
    for partition in generate_partitions(shoe_list):
        boxes = []
        for subset in partition:
            box = Box()  # create an empty box
            for shoe in subset:
                box.add_shoe(shoe)  # add each shoe to the box
            boxes.append(box)
        all_combinations.append(boxes)
    return all_combinations


def generate_partitions(lst):
    if len(lst) == 0:
        yield []
        return
    first = lst[0]
    for smaller in generate_partitions(lst[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n + 1 :]
        # put `first` in its own subset
        yield [[first]] + smaller


def print_combinations(all_combinations):
    for i, combinations in enumerate(all_combinations, 1):
        print(f"SOLUTION : {i}:")
        for j, box in enumerate(combinations, 1):
            print(f"Box {j} contains:")
            print(f"Price: {box.price}")
            for shoe in box.shoes:
                print(shoe.name)
    print("\n")
