class Box:
    def __init__(self, shoes=None):
        if shoes is None:
            self.shoes = []
        else:
            self.shoes = shoes
        self.price = 0
        self.kids_size_counter = 0
        self.brands = []
        self.low_score_counter = 0
        self.high_score_counter = 0

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

        if shoe.max_size < 35:
            self.kids_size_counter += 1
        elif shoe.score < 5:
            self.low_score_counter += 1
        elif shoe.score > 8:
            self.high_score_counter += 1

        self.brands.append(shoe.name)

        self.price += shoe.price

    def remove_shoe(self, shoe):
        self.shoes.remove(shoe)

        if shoe.max_size < 35:
            self.kids_size_counter -= 1
        elif shoe.score < 5:
            self.low_score_counter -= 1
        elif shoe.score > 8:
            self.high_score_counter -= 1

        self.brands.remove(shoe.name)

        self.price -= shoe.price

    def calculate_price(self):

        #print("CALCULATING PRICE")
        #print("INITIAL PRICE " + str(self.price))
        #print(
        #    "ALL COUNTERS "
        #    + str(self.kids_size_counter)
        #    + " "
        #    + str(self.low_score_counter)
        #    + " "
        #    + str(self.high_score_counter)
        #)
        self.price = 0
        for shoe in self.shoes:
            discount = 1
            #print(shoe.name)
            #print(shoe.price)

            if self.brands.count(shoe.name) >= 2:
                discount -= 0.2
            if self.kids_size_counter >= 2:
                discount -= 0.35
            if self.low_score_counter >= 3:
                discount -= 0.4
            if self.high_score_counter >= 3:
                discount += 0.2

            final_price = shoe.price * discount
            #print("DISCOUNT " + str(discount))
            #print("FINAL PRICE " + str(final_price))
            self.price += final_price

        #print("BOX FINAL PRICE: "+ str(self.price))
