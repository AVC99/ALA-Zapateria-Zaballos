from model.Shoe import *
from model.Node import Node
import time
from collections import deque


def IP_start_branch_and_bound(shoe_list):
    print("Branch and Bound started")
    time_start = time.time()

    n = len(shoe_list)
    best_difference = float("inf")
    best_part1 = []
    best_part2 = []

    # Initialize the node queue
    queue = deque([Node(0, [], [], 0, 0, 0)])

    while queue:
        node = queue.popleft()

        if node.index == n:
            # Check and update the best solution found
            if node.difference < best_difference:
                best_difference = node.difference
                best_part1 = node.part1.copy()
                best_part2 = node.part2.copy()
        else:
            # Generate child nodes
            for i in range(2):
                new_part1 = (
                    node.part1 + [shoe_list[node.index]] if i == 0 else node.part1
                )
                new_part2 = (
                    node.part2 + [shoe_list[node.index]] if i == 1 else node.part2
                )

                new_price_part1 = (
                    node.price_part1 + shoe_list[node.index].price
                    if i == 0
                    else node.price_part1
                )
                new_price_part2 = (
                    node.price_part2 + shoe_list[node.index].price
                    if i == 1
                    else node.price_part2
                )

                new_difference = abs(new_price_part1 - new_price_part2)

                # Add child nodes to the queue if they meet the condition
                if new_difference < best_difference:
                    queue.append(
                        Node(
                            node.index + 1,
                            new_part1,
                            new_part2,
                            new_price_part1,
                            new_price_part2,
                            new_difference,
                        )
                    )

    time_end = time.time()
    print("Branch and Bound ended")
    print(f"Execution Time: {time_end - time_start} seconds")

    # Display the results
    print("\n--------------------------------")
    print("Inventory division using Branch and Bound")
    print("--------------------------------")
    print(f"💰  Best price difference: €{best_difference:.2f}")

    total_price_part1 = sum(s.price for s in best_part1)
    print("\n🏪  Store 1 Inventory (Total Price: €{:.2f}):".format(total_price_part1))
    for s in best_part1:
        print(f"   👟  {s.name} - €{s.price}")

    total_price_part2 = sum(s.price for s in best_part2)
    print("\n🏪  Store 2 Inventory (Total Price: €{:.2f}):".format(total_price_part2))
    for s in best_part2:
        print(f"   👟  {s.name} - €{s.price}")

    print("--------------------------------\n")

    return best_part1, best_part2
