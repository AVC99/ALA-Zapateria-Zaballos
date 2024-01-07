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
    box_counter = 0
    # Generate all possible combinations of boxes for each shoe
    all_combinations = generate_shoe_combinations(shoe_list)
    # Print all the combinations
    print_combinations(all_combinations)


    time_end = time.time()
    print("Bruteforce ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")
    print("Box counter: " + str(box_counter))


def generate_shoe_combinations(shoe_list):
    all_combinations = []
    for partition in generate_partitions(shoe_list):
        boxes = [Box(shoes=subset) for subset in partition]
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
            yield smaller[:n] + [[first] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [[first]] + smaller

def print_combinations(all_combinations):
    for i, combinations in enumerate(all_combinations, 1):
        print(f"SOLUTION : {i}:")
        for j, box in enumerate(combinations, 1):
            print(f"Box {j} contains:")
            for shoe in box.shoes:
                print(shoe.name)
    print("\n");


