class Box:
    def __init__(self):
        self.shoes = set()
        self.price = 0
        self.kids_size_counter = 0
        self.brands = []
        self.low_score_counter = 0
        self.high_score_counter = 0

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

        if shoe.size < 35:
            self.kids_size_counter += 1
        elif shoe.score < 5:
            self.low_score_counter += 1
        elif shoe.score > 8:
            self.high_score_counter += 1

        self.brands.append(shoe.brand)

        self.price += shoe.price

    def remove_shoe(self, shoe):
        self.shoes.remove(shoe)

        if shoe.size < 35:
            self.kids_size_counter -= 1
        elif shoe.score < 5:
            self.low_score_counter -= 1
        elif shoe.score > 8:
            self.high_score_counter -= 1

        self.brands.remove(shoe.brand)

        self.price -= shoe.price
