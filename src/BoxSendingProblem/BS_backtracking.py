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

    def backtrack(boxes, remaining_shoes):
        nonlocal best_solution, best_box_count

        # Check if the current solution is valid and update best_solution if it's better
        if not remaining_shoes:
            current_box_count = len(boxes)
            if current_box_count < best_box_count:
                best_box_count = current_box_count
                best_solution = copy.deepcopy(boxes)
            return

        for shoe in remaining_shoes:
            # Try to fit the shoe in existing boxes
            for box in boxes:
                if len(box.shoes) < 6:
                    box.add_shoe(shoe)
                    box.calculate_price()  # Calculate price after adding the shoe
                    if box.price < 1000:
                        backtrack(boxes, [s for s in remaining_shoes if s != shoe])
                    box.remove_shoe(shoe)  # Remove the shoe and reset the price
                    box.calculate_price()  # Recalculate price after removing the shoe

            # Try adding a new box if it doesn't exceed the current best solution
            if len(boxes) < best_box_count:
                new_box = Box()
                new_box.add_shoe(shoe)
                if new_box.price < 1000:
                    backtrack(
                        boxes + [new_box], [s for s in remaining_shoes if s != shoe]
                    )

    # Start the backtracking process
    backtrack([], shoe_list)

    # Output the best solution
    print_best_solution(best_solution)

    time_end = time.time()
    print("Backtracking ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")


def print_best_solution(best_solution):
    if best_solution is None:
        print("No valid solution found")
        return

    print("Best solution using backtracking:")
    for i, box in enumerate(best_solution, 1):
        print(f"Box {i} contains:")
        for shoe in box.shoes:
            print(shoe.name)
        print(f"Price: {box.price}")
