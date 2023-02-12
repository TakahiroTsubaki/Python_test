from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, cal):
        self.name = name
        self.price = price
        self.cal = cal

    def info(self):
        return self.name + ': ¥' + str(self.price) + " " + "("+ str(self.cal) + "kcal" + ")"

    