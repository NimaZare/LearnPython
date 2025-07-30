import random

calss Hat():

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # def sort(self, name):
    #     print(name, "is in", random.choice(self.houses))

    # like  static methods in c#
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# hat = Hat()
# hat.sort("Harry")

Hat.sort("Harry")
