from model.Shoe import *
from model.Box import *
import time
import copy


def BS_start_backtracking(shoe_list):
    print("Backtracking started")
    time_start = time.time()

    # Initialize variables for tracking the best solution
    best_solution = None  # Stores the best combination of boxes found so far
    best_box_count = float("inf")  # Stores the count of boxes in the best solution

    def backtrack(boxes, remaining_shoes, box_count):
        nonlocal best_solution, best_box_count

        # Early pruning: Stop if the current number of boxes is already not better than the best found
        if box_count >= best_box_count:
            return

        # Check if all shoes have been placed. If yes, update the best solution if it's better than the current best
        if not remaining_shoes:
            if box_count < best_box_count:
                best_box_count = box_count
                best_solution = copy.deepcopy(
                    boxes
                )  # Deep copy to avoid mutating the best solution
            return

        for i, shoe in enumerate(remaining_shoes):
            # Iterate over existing boxes
            for box in boxes:
                if len(box.shoes) < 6:  # Check box capacity
                    box.add_shoe(shoe)
                    box.calculate_price()  # Recalculate price with the new shoe
                    if box.price < 1000:  # Ensure the box price is within the limit
                        new_remaining = remaining_shoes[:i] + remaining_shoes[i + 1 :]
                        backtrack(boxes, new_remaining, box_count)
                    box.remove_shoe(shoe)
                    box.calculate_price()

            # Add a new box if it doesn't exceed the current best solution
            if box_count + 1 < best_box_count:
                new_box = Box()
                new_box.add_shoe(shoe)
                new_remaining = remaining_shoes[:i] + remaining_shoes[i + 1 :]
                backtrack(boxes + [new_box], new_remaining, box_count + 1)

    backtrack([], shoe_list, 0)

    print_best_solution(best_solution)
    time_end = time.time()
    print("Backtracking ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")


def print_best_solution(best_solution):
    if best_solution is None:
        print("No valid solution found")
        return
    print("")
    print("----------------------------------")
    print("Best solution using backtracking:")
    for i, box in enumerate(best_solution, 1):
        print(f"📦  BOX {i} contains:")
        for shoe in box.shoes:
            print("   👟 ", shoe.name)
        print(f"   💰  Price: {box.price}€")
    print("")
