class Chai:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size


class GingerChai(Chai):
    # code duplication
    # def __init__(self, type_, size,taste):
    #     self.type=type_
    #     self.size=size
    #     self.taste=taste

    # explicit call
    # def __init__(self, type_, size,taste):
    #     Chai.__init__(self,type_,size)
    #     self.taste=taste

    # final super method
    def __init__(self, type_, size, taste):
        super().__init__(type_, size)
        self.taste = taste

    def output(self):
        print(
            f"Type of chai is {self.type} Size of the Chai is {self.size} and finally the taste of the chai is {self.taste}"
        )


chai = GingerChai("Lemon Chai", 200, "Yammy")
chai.output()
