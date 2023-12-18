from model.Shoe import *
from model.Box import *
from itertools import permutations
from itertools import product
import time
import math

# DUBTES:
# Totes les sabates tenen que estar colocades? Entenc que si
# Ha de estar les capeses plenes? Entenc que no


def BS_start_bruteforce(shoe_list):
    print("Bruteforce started")
    time_start = time.time()

    # Create all the possible combinations of boxes
    all_combinations = generate_all_combinations(shoe_list)
    print_all_combinations(all_combinations)

    time_end = time.time()
    print("Bruteforce ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")


def generate_all_combinations(shoe_dataset):
    all_combinations = []

    def generate_combinations_recursive(box, shoe_index):
        if shoe_index == len(shoe_dataset):
            # Reached the end of the shoe dataset, add the current box
            all_combinations.append(Box(shoes=box.shoes[:], price=box.price))
            return

        # Skip the current shoe and move to the next one
        generate_combinations_recursive(box, shoe_index + 1)

        # Include the current shoe in the box and move to the next shoe
        box.add_shoe(shoe_dataset[shoe_index])
        generate_combinations_recursive(box, shoe_index + 1)
        box.remove_shoe(shoe_dataset[shoe_index])

    generate_combinations_recursive(Box(), 0)
    return all_combinations




def print_all_combinations(all_combinations):
    for i, box in enumerate(all_combinations, 1):
        print(f"Box {i}:")
        for shoe in box.shoes:
            print(f"  {shoe.name} - ${shoe.price}")
        print(f"  Total Price: ${box.price}")
        print()


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
