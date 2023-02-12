from menu_item import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, ml):
        self.name = name
        self.price = price
        self.ml = ml

    def info(self):
        return self.name + ': ¥' + str(self.price) + " " + "("+ str(self.ml) + "ml" + ")"
