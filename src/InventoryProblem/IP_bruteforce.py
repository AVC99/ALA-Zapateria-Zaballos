from model.Shoe import *
from itertools import permutations, combinations
import time

def IP_start_bruteforce(shoe_list):
    print("Bruteforce started")
    time_start = time.time()
    n = len(shoe_list)
    millor_diferencia = float('inf')
    millor_part1 = []
    millor_part2 = []

   # El bucle ha de començar des de 0 per incloure totes les sabates a la primera botiga
    for i in range(n + 1):
        #permutations miro el: 123, 132, 321
        #combinations miro el: 123, 124, 125, 126
        permutacions = combinations(shoe_list, i)
        for perm in permutacions:
          
          part1 = list(perm)
          part2 = [s for s in shoe_list if s not in part1]

          preu_part1 = sum(s.price for s in part1)
          preu_part2 = sum(s.price for s in part2)

          diferencia = abs(preu_part1 - preu_part2)

          if diferencia < millor_diferencia:
                millor_diferencia = diferencia
                millor_part1 = part1
                millor_part2 = part2

    time_end = time.time()
    print(time_end - time_start)

    print("Millor diferencia: ", millor_diferencia)
    print("La mejor parte 1: " )
    for s in millor_part1:
        print(s.name, s.price)
    print("La mejor parte 2: ")
    for s in millor_part2:
        print(s.name, s.price)

    return millor_part1, millor_part2


# Exemple d'ús:
'''part1, part2 = IP_start_bruteforce(shoe_list)
print("Botiga 1:")
for s in part1:
    print(s.name, s.price)

print("\nBotiga 2:")
for s in part2:
    print(s.name, s.price)
 '''