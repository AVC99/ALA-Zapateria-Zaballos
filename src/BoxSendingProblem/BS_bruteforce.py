from model.Shoe import *
from model.Box import *
import time
import copy


def BS_start_bruteforce(shoe_list):
    print("Bruteforce started")
    time_start = time.time()
    # Generate all possible combinations of boxes for each shoe
    all_combinations, box_counter = generate_shoe_combinations(shoe_list)

    recalculate_price(all_combinations)
    print("Recalculated prices")

    best_price, best_combination = find_best_solution(all_combinations)

    print_best_combination(best_combination, best_price)

    time_end = time.time()
    print("Bruteforce ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")
    print("Box counter: " + str(box_counter))


def print_best_combination(best_combination, best_price):
    print("\n------------------")
    print("Best solution:")
    for j, box in enumerate(best_combination, 1):
        print(f"📦 Box {j} contains:")
        for shoe in box.shoes:
            print("   👟 ", shoe.name  ," price: ", shoe.price)
        print(f"Box price: {box.price}")
    print(f"Total Price: {best_price}")
    print(f"Total Boxes: {len(best_combination)}")
    print("------------------\n")


def find_best_solution(all_combinations):
    best_price = float("inf")
    best_boxes = float("inf")
    best_combination = []

    for i, combinations in enumerate(all_combinations, 1):
        combination_price = 0
        comb_boxes = 0
        for j, box in enumerate(combinations, 1):
            if box.price >= 1000:
                print("Box price is too high")
                combination_price = float("inf")
                comb_boxes = float("inf")
                break  # skip this box but continue with the next box
            elif combination_price + box.price >= best_price:
                print(
                    "Combination price is too high I have found a better solution"
                )  # skip this box and all the next boxes
                combination_price = float("inf")
                comb_boxes = float("inf")
                break
            else:
                combination_price += box.price
                comb_boxes += 1

        # if the total price of this combination is higher than the best price found so far
        if comb_boxes < best_boxes:
            best_price = copy.deepcopy(combination_price)
            best_combination = copy.deepcopy(combinations)

    return best_price, best_combination


def recalculate_price(all_combinations):
    for i, combinations in enumerate(all_combinations, 1):
        for j, box in enumerate(combinations, 1):
            box.calculate_price()


def generate_shoe_combinations(shoe_list):
    all_combinations = []
    box_counter = 0
    for partition in generate_partitions(shoe_list):
        boxes = []
        for subset in partition:
            box = Box()  # create an empty box
            box_counter += 1
            for shoe in subset:
                # if the box has less than 6 shoes
                if len(box.shoes) < 6:
                    box.add_shoe(shoe)  # add each shoe to the box

            boxes.append(box)
        all_combinations.append(boxes)
    return all_combinations, box_counter


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
