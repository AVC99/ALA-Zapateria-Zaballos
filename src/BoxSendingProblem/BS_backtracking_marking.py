from model.Shoe import *
from model.Box import *
import time
import copy


def BS_start_backtracking_marking(shoe_list):
    print("Backtracking started")
    time_start = time.time()

    # Initialize variables for tracking the best solution
    best_solution = None  # Stores the best combination of boxes found so far
    best_box_count = float("inf")  # Stores the count of boxes in the best solution
    visited_states = set()  # For marking

    def state_identifier(boxes):
        # Generate a unique identifier for the current state
        return tuple(
            sorted(
                (
                    shoe.name,
                    shoe.price,
                    shoe.min_size,
                    shoe.max_size,
                    shoe.weight,
                    shoe.score,
                )
                for box in boxes
                for shoe in box.shoes
            )
        )

    def backtrack(boxes, remaining_shoes, box_count):
        nonlocal best_solution, best_box_count

        state_id = state_identifier(boxes)
        if state_id in visited_states:  # Skip already visited states
            return
        visited_states.add(state_id)

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
    print("Time elapsed: {:.5f} seconds".format(time_end - time_start))


def print_best_solution(best_solution):
    if best_solution is None:
        print("No valid solution found")
        return

    total_price = 0  # To accumulate the total price of all boxes
    box_count = len(best_solution)  # Total number of boxes used

    print("\n----------------------------------")
    print("Best solution using backtracking:")
    for i, box in enumerate(best_solution, 1):
        print(f"📦  BOX {i} contains:")
        for shoe in box.shoes:
            print("   👟 ", shoe.name)
        print(f"   💰  Price: {box.price}€\n")
        total_price += box.price  # Add the price of this box to the total

    print("----------------------------------")
    print(f"Total number of boxes used: {box_count}")
    print(f"Total combined price of all boxes: {total_price}€")
    print("----------------------------------\n")
