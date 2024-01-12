from model.Shoe import *


def getDatasetName(dataset_option):
    if dataset_option == "1":
        return "data/datasets/datasetXXS.txt"
    elif dataset_option == "2":
        return "data/datasets/datasetXS.txt"
    elif dataset_option == "3":
        return "data/datasets/datasetS.txt"
    elif dataset_option == "4":
        return "data/datasets/datasetM.txt"
    elif dataset_option == "5":
        return "data/datasets/datasetL.txt"
    elif dataset_option == "6":
        return "data/datasets/datasetXXXL.txt"


def getShoes(dataset_option):
    shoes = []
    dataset = getDatasetName(dataset_option)
    with open(dataset, "r") as f:
        n_of_shoes = f.readline()
        for x in range(int(n_of_shoes)):
            parts = f.readline().split(";")
            name = parts[0]
            price = float(parts[1].replace(",", "."))
            min_size = int(parts[2])
            max_size = int(parts[3])
            weight = int(parts[4])
            score = float(parts[5].replace(",", "."))

            shoe = Shoe(name, price, min_size, max_size, weight, score)
            shoes.append(shoe)

    return shoes
