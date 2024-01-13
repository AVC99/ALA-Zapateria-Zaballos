from model.Shoe import *
from model.Box import *
import time
import copy



def BS_start_branch_and_bound(shoe_list):
    print("STARTING BRANCH AND BOUND")
    start_time = time.time()
    best_solution = branch_and_bound(shoe_list)

    print_best_solution(best_solution)
    final_time = time.time()
    print("Time elapsed: " + str(final_time - start_time) + " seconds")


def branch_and_bound(shoe_list):
    valid_solutions_counter = 0
    configs = []
    configs.append(([Box()], shoe_list))  # 0,1 -> boxes, remaining_shoes, price
    best_solution = None
    min_boxes = float("inf")

    while configs:
        configs.sort(key=lambda x: len(x[0]), reverse=True)
        current_config = configs.pop()
        sons = expand(current_config)

        for son in sons:
            if len(son[0]) < min_boxes:
                configs.append(son)
                total_shoes_in_boxes = sum([len(box.shoes) for box in son[0]])
                if total_shoes_in_boxes == len(shoe_list):  # If all shoes are in boxes => valid solution
                    min_boxes = copy.deepcopy(len(son[0]))
                    best_solution = copy.deepcopy(son[0])

                    valid_solutions_counter += 1

    return best_solution


def expand(current_config):
    sons = []
    boxes, remaining_shoes = current_config

    for i, shoe_to_add in enumerate(remaining_shoes):
        if i > 0:
            # Skip shoes that have been considered in previous iterations
            continue

        for j, box in enumerate(boxes):
            if len(box.shoes) < 6:
                new_box = copy.deepcopy(box)
                new_box.add_shoe(shoe_to_add)
                new_box.calculate_price()

                if new_box.price <= 1000:
                    new_boxes = copy.deepcopy(boxes[:j] + [new_box] + boxes[j + 1 :])
                    new_remaining_shoes = remaining_shoes[i + 1 :]
                    sons.append((new_boxes, new_remaining_shoes))

        new_box = Box()
        new_box.add_shoe(shoe_to_add)
        new_box.calculate_price()
        if new_box.price <= 1000:
            new_boxes = copy.deepcopy(boxes + [new_box])
            new_remaining_shoes = remaining_shoes[i + 1 :]
            sons.append((new_boxes, new_remaining_shoes))
    return sons


def print_best_solution(best_combination):
    price = 0
    print("\n------------------")
    print("Best solution:")
    for j, box in enumerate(best_combination, 1):
        print(f"📦 Box {j} contains:")
        for shoe in box.shoes:
            print("   👟 ", shoe.name  ," price: ", shoe.price)
        price += box.price
        print(f"Box price: {box.price}")
    print(f"Total price: {price}")
    print(f"Total Boxes: {len(best_combination)}")
    print("------------------\n")
