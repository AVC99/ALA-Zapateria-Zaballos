from model.Shoe import *
from model.Box import *
from itertools import combinations
import time
import math

# DUBTES:
# Totes les sabates tenen que estar colocades? Entenc que si
# Ha de estar les capeses plenes? Entenc que no


def BS_start_bruteforce(shoe_list):
    print("Bruteforce started")
    time_start = time.time()
    # Generate all possible combinations of boxes for each shoe
    all_combinations = generate_shoe_combinations(shoe_list)
    # Print all the combinations
    print_combinations(all_combinations)
    time_end = time.time()
    print("Bruteforce ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")


def generate_shoe_combinations(shoe_list):
    all_combinations = []
    for r in range(1, len(shoe_list) + 1):
        r_combinations = []
        for comb in combinations(shoe_list, r):
            box = Box()
            for shoe in comb:
                box.add_shoe(shoe)
            r_combinations.append(box)
        all_combinations.append(r_combinations)
    return all_combinations

def print_combinations(all_combinations):
    for i, combinations in enumerate(all_combinations, 1):
        print(f"sol{i}:")
        for j, box in enumerate(combinations, 1):
            print(f"Box {j} contains:")
            for shoe in box.shoes:
                print(shoe.name)





# Im not using this function rn the idea is to use it later on when i actually have the code working
def calculate_configuration_price(configuration, shoe_list):
    for box in configuration:
        newprice = 0
        same_brand_counter = 0
        kids_size_counter = 0
        low_score_counter = 0
        high_score_counter = 0
        for i in range(len(box.shoes)):
            for j in range(len(shoe_list)):
                if box.shoes[i].name == shoe_list[j].name:
                    same_brand_counter += 1

            if is_kids_size(box.shoes[i]):
                kids_size_counter += 1
            if is_low_score(box.shoes[i]):
                low_score_counter += 1
            if is_high_score(box.shoes[i]):
                high_score_counter += 1
            if same_brand_counter >= 2:
                box.shoes[i].price *= 0.2
            if kids_size_counter >= 2:
                box.shoes[i].price *= 0.35
            if low_score_counter >= 3:
                box.shoes[i].price *= 0.4
            if high_score_counter >= 3:
                box.shoes[i].price *= 1.2
            newprice += box.shoes[i].price

        box.price = newprice

    return configuration


def is_kids_size(shoe):
    return shoe.max_size < 35


def is_low_score(shoe):
    return shoe.score < 5


def is_high_score(shoe):
    return shoe.score > 8
