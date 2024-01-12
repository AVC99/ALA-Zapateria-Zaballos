from model.Shoe import *
import time
#OSCAR



#Porque tarda mas que el de fuerza bruta?



class Node:
    def __init__(self, index, part1, part2, preu_part1, preu_part2, diferencia):
        self.index = index
        self.part1 = part1
        self.part2 = part2
        self.preu_part1 = preu_part1
        self.preu_part2 = preu_part2
        self.diferencia = diferencia

def IP_start_branch_and_bound(shoe_list):
    print("Branch and Bound started")
    time_start = time.time()

    n = len(shoe_list)
    millor_diferencia = float('inf')
    millor_part1 = []
    millor_part2 = []

    # Inicializar la cola de nodos
    queue = [Node(0, [], [], 0, 0, 0)]

    while queue:
        node = queue.pop(0)

        if node.index == n:
            # Verificar y actualizar la mejor solución encontrada
            if node.diferencia < millor_diferencia:
                millor_diferencia = node.diferencia
                millor_part1 = node.part1.copy()
                millor_part2 = node.part2.copy()

        else:
            # Generar nodos hijos
            for i in range(2):
                new_part1 = node.part1 + [shoe_list[node.index]] if i == 0 else node.part1
                new_part2 = node.part2 + [shoe_list[node.index]] if i == 1 else node.part2

                new_preu_part1 = node.preu_part1 + shoe_list[node.index].price if i == 0 else node.preu_part1
                new_preu_part2 = node.preu_part2 + shoe_list[node.index].price if i == 1 else node.preu_part2

                new_diferencia = abs(new_preu_part1 - new_preu_part2)

                # Agregar nodos hijos a la cola si cumplen con la condición
                if new_diferencia < millor_diferencia:
                    queue.append(Node(node.index + 1, new_part1, new_part2, new_preu_part1, new_preu_part2, new_diferencia))

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
