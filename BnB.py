from queue import PriorityQueue
import model.Shoe as Shoe
class Box:
    def __init__(self, shoes=None):
        if shoes is None:
            shoes = []
        self.shoes = shoes
        self.price = 0
        self.best_solution = float('-inf')

    def branch_and_bound(self, remaining_shoes):
        priority_queue = PriorityQueue()

        # Initial node representing an empty box
        initial_node = {"shoes": [], "price": 0}
        priority_queue.put((-initial_node["price"], initial_node))

        while not priority_queue.empty():
            _, node = priority_queue.get()
            
            for shoe in remaining_shoes:
                child_node = {"shoes": node["shoes"] + [shoe], "price": node["price"] + shoe.price}

                # Apply feasibility checks here (constraints on the number of shoes, weight, etc.)

                # Update the best solution
                if child_node["price"] > self.best_solution:
                    self.best_solution = child_node["price"]

                # Add the child node to the priority queue
                priority_queue.put((-child_node["price"], child_node))

        # Set the final best solution to the box price
        self.price = self.best_solution

# Example usage:
# Create shoes and box objects
shoe1 = Shoe("Nike", 100, 30, 40, 0.5, 7)
shoe2 = Shoe("Adidas", 120, 35, 45, 0.6, 8)
shoe3 = Shoe("Puma", 80, 25, 35, 0.4, 6)

shoes = [shoe1, shoe2, shoe3]
box = Box()

# Call the branch and bound algorithm
box.branch_and_bound(shoes)

# Print the final box price
print("Optimal Box Price:", box.price)
