from model.Shoe import *
from model.Box import *
import time
import math


def BS_start_bruteforce(shoe_list):
    print("Bruteforce started")
    time_start = time.time()

    configuration = create_initial_configuration(shoe_list)
    best_configuration = configuration

   

    bruteforce(configuration, best_configuration, shoe_list)   


   
    

    time_end = time.time()
    print("Bruteforce ended")
    print("Time elapsed: " + str(time_end - time_start) + " seconds")


def create_initial_configuration(shoe_list):
    # configuration is a list of boxes 
    # each box is a list of shoes
    # each shoe is a Shoe object
    configuration = [Box() for _ in range(math.ceil(len(shoe_list) / 6))]

    shoe_counter = 0
    box_counter = 0
    for shoe in shoe_list:
        configuration[box_counter].add_shoe(shoe)
        shoe_counter += 1
        if shoe_counter == 6:
            shoe_counter = 0
            box_counter += 1
        
    return configuration
    
def bruteforce(configuration, best_configuration, shoe_list):
    

    for box in configuration:
        same_brand_counter = 0
        kids_size_counter = 0
        low_score_counter = 0
        high_score_counter = 0
        for i in box.shoes.length:
            for j in shoe_list.length:
                if box.shoes[i].name == shoe_list[j].name:
                   same_brand_counter += 1

            if box.shoes[i].max_size < 35:
                kids_size_counter += 1
            if box.shoes[i].score < 5:
                low_score_counter += 1
            if box.shoes[i].score > 8:
                high_score_counter += 1
            if same_brand_counter >= 2:
                box.shoes[i].price *= 0.2
            if kids_size_counter >= 2:
                box.shoes[i].price *= 0.35
            if low_score_counter >= 3:
                box.shoes[i].price *= 0.4
            if high_score_counter >= 3:
                box.shoes[i].price *= 1.2
        
            
    
                


    return best_configuration