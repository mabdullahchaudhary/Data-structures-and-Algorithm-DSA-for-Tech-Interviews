class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"Size of the tea is {self.size} and the type is {self.type}"

    def calculate_price(self, value_1, value_2):
        return f"Actual price is the double of the size {value_1+value_2}"


cup = ChaiOrder("Masala Chai", 200)
print(cup.summary())
print(cup.calculate_price(30, 50))
