import model.Shoe as Shoe
import model.Box as Box
import time
import copy
from queue import PriorityQueue


def BS_start_branch_and_bound(shoe_list):
    start_time = time.time()
    print("Branch and bound started")
    # Start branch and bound 
    best_configuration = branch_and_bound(shoe_list)

    print_best_configuration(best_configuration)
    
    end_time = time.time()
    print("Branch and bound ended")
    print("Time elapsed: " + str(end_time - start_time) + " seconds")




def branch_and_bound(shoe_list):
    configs = []
    x = generate_initial_configuration(shoe_list)
    configs.append(x)
    configs.sort(key=lambda x: x.price)
    while configs:
        x = configs.pop(0)
        if x.price < 1000:
            x.print()
            for y in generate_children(x):
                configs.append(y)
                configs.sort(key=lambda x: x.price)

def generate_children(configuration):
    children = []
    for box in configuration.boxes:
        for shoe in box.shoes:
            new_configuration = copy.deepcopy(configuration)
            new_configuration.remove_shoe(shoe)
            children.append(new_configuration)
    return children

def generate_initial_configuration(shoe_list):
    boxes = []
    for shoe in shoe_list:
        box = Box()
        box.add_shoe(shoe)
        boxes.append(box)
    return boxes

def print_best_configuration(best_configuration):
    print("\n------------------")
    print("Best solution:")
    for j, box in enumerate(best_configuration, 1):
        print(f"📦 Box {j} contains:")
        for shoe in box.shoes:
            print("   👟 ", shoe.name," price: ", shoe.price)
        print(f"Box price: {box.price}")
    print(f"Total Price: {best_configuration.price}")
    print(f"Total Boxes: {len(best_configuration)}")
    print("------------------\n")