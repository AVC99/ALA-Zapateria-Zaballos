from data.shoeDAO import getShoes
from model.Shoe import *

from src.InventoryProblem.IP_bruteforce import IP_start_bruteforce
from src.InventoryProblem.IP_Backtacking import IP_start_backtracking
from src.InventoryProblem.IP_branch_and_bound import IP_start_branch_and_bound
from src.InventoryProblem.IP_greedy import IP_start_greedy

from src.BoxSendingProblem.BS_bruteforce import BS_start_bruteforce
from src.BoxSendingProblem.BS_backtracking import BS_start_backtracking
from src.BoxSendingProblem.BS_backtracking_marking import BS_start_backtracking_marking
from src.BoxSendingProblem.BS_branch_and_bound import BS_start_branch_and_bound
from src.BoxSendingProblem.BS_greedy import BS_start_greedy

import os


def printResolutionMethodsMenu():
    while True:
        print()
        print("Please, select an option:")
        print("1. Brute force")
        print("2. Backtracking")
        print("3. Branch and bound")
        print("4. Greedy")
        print("0. Exit")
        user_input = input("Enter your option: ")

        if user_input in ["0", "1", "2", "3", "4"]:
            return user_input
        else:
            print("Invalid option. Please enter a valid option.")


def printProblemsMenu():
    while True:
        print()
        print("Welcome to Zapateria Zaballos optimizer!!")
        print("Problems available:")
        print("1. Box sending problem")
        print("2. Inventory problem")
        print("0. Exit")
        user_input = input("Enter your option: ")

        if user_input in ["0", "1", "2"]:
            return user_input
        else:
            print("Invalid option. Please enter a valid option.")


def printDatasetSelectionMenu():
    while True:
        print()
        print("Please, select a dataset:")
        print("1. XXS")
        print("2. XS")
        print("3. S")
        print("4. M")
        print("5. L")
        print("6. XXXL")
        print("0. Exit")
        user_input = input("Enter your option: ")

        if user_input in ["0", "1", "2", "3", "4", "5", "6"]:
            return user_input
        else:
            print("Invalid option. Please enter a valid option.")


def printBacktrackingOptionsMenu():
    while True:
        print("\nSelect Backtracking Option:")
        print("1. Backtracking")
        print("2. Backtracking with Marking")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice in ["0", "1", "2"]:
            return choice
        else:
            print("Invalid option. Please enter a valid option.")


def main():
    problem_option = printProblemsMenu()

    if problem_option == "0":
        print("Exiting program.")
        return

    dataset_option = printDatasetSelectionMenu()
    if dataset_option == "0":
        print("Exiting program.")
        return

    try:
        shoe_list = getShoes(dataset_option)
    except FileNotFoundError:
        print(
            f"Error: Dataset file for the selected option ({dataset_option}) is not found."
        )
        return

    resolution_method = printResolutionMethodsMenu()
    if resolution_method == "0":
        print("Exiting program.")
        return

    if problem_option == "1":
        if resolution_method == "1":
            BS_start_bruteforce(shoe_list)
        elif resolution_method == "2":
            backtracking_option = printBacktrackingOptionsMenu()
            if backtracking_option == "1":
                BS_start_backtracking(shoe_list)
            elif backtracking_option == "2":
                BS_start_backtracking_marking(shoe_list)
        elif resolution_method == "3":
            BS_start_branch_and_bound(shoe_list)
        elif resolution_method == "4":
            BS_start_greedy(shoe_list)
    elif problem_option == "2":
        if resolution_method == "1":
            IP_start_bruteforce(shoe_list)
        elif resolution_method == "2":
            IP_start_backtracking(shoe_list)
        elif resolution_method == "3":
            IP_start_branch_and_bound(shoe_list)
        elif resolution_method == "4":
            IP_start_greedy(shoe_list)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("aborted")
