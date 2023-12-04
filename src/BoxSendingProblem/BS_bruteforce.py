from model.Shoe import *
from model.Box import *
from itertools import permutations
import time
import math

# DUBTES:
# Totes les sabates tenen que estar colocades? Entenc que si
# Ha de estar les capeses plenes? Entenc que no


def BS_start_bruteforce(shoe_list):
    print("Bruteforce started")
    time_start = time.time()

    configuration = create_initial_configuration(shoe_list)
    best_configuration = configuration

    best_configuration = bruteforce(configuration, best_configuration, shoe_list)

    #THIS IS NOT WORKING FOR NOW
    # print best configuration
    print("Best configuration:")
    for box in best_configuration:
        print("  Box:")
        for shoe in box.shoes:
            print("    " + shoe.name + " - $" + str(shoe.price))
        print("    Total Price: $" + str(box.price))

    time_end = time.time()
    print("Bruteforce ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")


# WHEN WE CREATE ALL THE COMBINATIONS I DONT THINK WE NEED THIS ANYMORE
def create_initial_configuration(shoe_list):
    # configuration is a list of boxes
    # each box is a list of shoes
    # each shoe is a Shoe object
    configuration = [Box() for _ in range(math.ceil(len(shoe_list) / 6))]

    shoe_counter = 0
    box_counter = 0
    for shoe in shoe_list:
        configuration[box_counter].add_shoe(shoe)
        shoe_counter += 1
        if shoe_counter == 6:
            shoe_counter = 0
            box_counter += 1

    return configuration


def bruteforce(configuration, best_configuration, shoe_list):
    best_configuration_total_price = 0

    all_box_combinations = set()

    for perm in permutations(shoe_list):
        boxes = []
        remaining_price = 1000
       #Could bake into this the discount calculations I should indeed do that
       #TODO: Calculate the discounts
        for shoe in perm:
            if remaining_price - shoe.price >= 0:
                remaining_price -= shoe.price
                if len(boxes) == 0:
                    boxes.append(Box())
                boxes[-1].add_shoe(shoe)
            else:
                boxes.append(Box())
                boxes[-1].add_shoe(shoe)
                remaining_price = 1000 - shoe.price
        all_box_combinations.add(tuple(boxes))

    # Print all_box_combinations before recalculating prices
    for config_num, config in enumerate(all_box_combinations, 1 ):
        print(f"Configuration {config_num}:")
        for box_num, box in enumerate(config, 1):
            print(f"  Box {box_num}:")
            for shoe in box.shoes:
                print(f"    {shoe.name} - ${shoe.price}")
            print(f"    Total Price: ${box.price}")
        print()


    """
    #FROM HERE ON IS WRONG ------------------------------------
    # Recalculate configuration prices with the discounts
    for config_num, config in enumerate(all_box_combinations, 1 ):
        print(f"Configuration {config_num}:")
        for box_num, box in enumerate(config, 1):
            newprice = 0
            same_brand_counter = 0
            kids_size_counter = 0
            low_score_counter = 0
            high_score_counter = 0

            for i in range(len(box.shoes)):
                for j in range(len(box.shoes)):
                    if box.shoes[i].name == box.shoes[j].name:
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
            print(f"  Box {box_num}:")
            for shoe in box.shoes:
                print(f"    {shoe.name} - ${shoe.price}")
            print(f"    Total Price: ${box.price}")
        print()

    # Calculate total price for the configuration
    for config in all_box_combinations:
        total_price = 0
        for box in config:
            total_price += box.price
        print(f"Total Price for all boxes: ${total_price}")
        print()

    """
    return best_configuration

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
