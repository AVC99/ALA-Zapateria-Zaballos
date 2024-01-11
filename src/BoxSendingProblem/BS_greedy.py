from model.Shoe import *
from model.Box import *
import time


def BS_start_greedy(shoe_list):
    print("Greedy approach started")
    time_start = time.time()

    # Heuristic 1: Sorts shoes by descending order of price.
    # Fills each box with the most expensive shoes first, maximizing the box's value
    # Higher efficiency
    shoe_list.sort(key=lambda shoe: shoe.price, reverse=True)

    # Heuristic 2: Sorts shoes by brand, prioritizes children's shoes, and considers shoe scores.
    # Maximizes the utilization of discounts and minimize surcharges.
    # Lower efficiency than the first heuristic, but provides a lower amount of boxes.
    # shoe_list.sort(key=lambda shoe: (shoe.name.split()[0], shoe.max_size < 35, -shoe.score))

    boxes = []
    current_box = Box()

    for shoe in shoe_list:
        # Check if the shoe can be added without exceeding box limits
        current_box.add_shoe(shoe)
        current_box.calculate_price()
        if len(current_box.shoes) <= 6 and current_box.price < 1000:
            # Shoe fits in the current box, continue
            continue
        else:
            # Shoe does not fit, start a new box
            current_box.remove_shoe(shoe)  # Remove the last shoe added
            current_box.calculate_price()
            boxes.append(current_box)  # Save the filled box
            current_box = Box()  # Start a new box
            current_box.add_shoe(shoe)  # Add the shoe to the new box
            current_box.calculate_price()

    # Add the last box if it has any shoes
    if current_box.shoes:
        boxes.append(current_box)

    time_end = time.time()
    print_greedy_solution(boxes)
    print("Greedy approach ended")
    print("Time elapsed: {:.5f} seconds".format(time_end - time_start))


def print_greedy_solution(boxes):
    box_count = len(boxes)
    total_price = sum(box.price for box in boxes)

    print("\n----------------------------------")
    print("Greedy solution result:")
    for i, box in enumerate(boxes, 1):
        print(f"📦  BOX {i} contains:")
        for shoe in box.shoes:
            print("   👟 ", shoe.name)
        print(f"   💰  Price: {box.price}€\n")

    print("----------------------------------")
    print("Total number of boxes used:", box_count)
    print("Total combined price of all boxes: {:.2f}€".format(total_price))
    print("----------------------------------\n")
