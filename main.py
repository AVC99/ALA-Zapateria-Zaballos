from shoeDAO import *

def printMenu():
  print("Welcome to Zapateria Zaballos optimizer!!")
  print("Please, select an option:")
  print("1. Brute force")
  print("2. Backtracking")
  print("3. Branch and bound")
  print("4. Greedy")
  print("0.Exit")
  return input("Select an option: ")
  

user_selection = printMenu()
while user_selection != "0":
  if user_selection == "1":
    #clear console
    getShoes()
    print("Brute force")
  elif user_selection == "2":
    print("Backtracking")
  elif user_selection == "3":
    print("Branch and bound")
  elif user_selection == "4":
    print("Greedy")
  else:
    print("Invalid option")
  user_selection = printMenu()