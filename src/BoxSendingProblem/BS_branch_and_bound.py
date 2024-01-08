import model.Shoe as Shoe
import model.Box as Box
import time
import copy


def BS_start_branch_and_bound(shoe_list):
    start_time = time.time()
    print("Branch and bound started")
    # Start branch and bound 
    best_configuration = branch_and_bound(shoe_list)




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