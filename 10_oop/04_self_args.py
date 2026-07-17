class Chaicup:
    size = 100  # ml

    def decribe(self):
        return f"Size of the Chaicup is {self.size}"


cup = Chaicup()
cup.size = 1000
print(cup.decribe())

print(Chaicup.decribe(cup))
