class Box:
  def __init__(self):
    self.shoes = [] * 6
    self.price = 0

  def add_shoe(self, shoe):
    self.shoes.append(shoe)
    self.price += shoe.price

  def remove_shoe(self, shoe):
    self.shoes.remove(shoe)
    self.price -= shoe.price
   