from model.Shoe import *
import time
#OSCAR

def IP_start_backtracking(shoe_list):
    def backtrack(index, part1, part2):
        nonlocal millor_diferencia, millor_part1, millor_part2

        if index == len(shoe_list):
            # Calcular la diferencia de precios y actualizar la mejor solución
            diferencia = abs(sum(s.price for s in part1) - sum(s.price for s in part2))
            if diferencia < millor_diferencia:
                millor_diferencia = diferencia
                millor_part1 = part1.copy()
                millor_part2 = part2.copy()

        else:
            # Incluir el zapato en la primera parte y explorar
            part1.append(shoe_list[index])
            backtrack(index + 1, part1, part2)
            part1.pop()  # Retroceder

            # Incluir el zapato en la segunda parte y explorar
            part2.append(shoe_list[index])
            backtrack(index + 1, part1, part2)
            part2.pop()  # Retroceder

    print("Backtracking started")
    time_start = time.time()
    
    millor_diferencia = float('inf')
    millor_part1 = []
    millor_part2 = []

    # Iniciar la recursión desde el índice 0
    backtrack(0, [], [])

    time_end = time.time()
    print(time_end - time_start)

    print("Millor diferencia: ", millor_diferencia)
    print("La mejor parte 1: ")
    for s in millor_part1:
        print(s.name, s.price)
    print("La mejor parte 2: ")
    for s in millor_part2:
        print(s.name, s.price)

    return millor_part1, millor_part2
