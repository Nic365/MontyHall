import random

class Game:
    def __init__(self):
        self.door1 = 0
        self.door2 = 0
        self.door3 = 0

        tresor = random.randint(1,3)

        if tresor == 1:
            self.door1 = 1
        elif tresor == 2:
            self.door2 = 1
        elif tresor == 3:
            self.door3 = 1

    def make_choice(self, choice):
        self.choice = choice

    def check_result(self):
        if self.choice == 1:
            if self.door1 == 1:
                print("You win")
            else:
                print("You loose")
        elif self.choice == 2:
            if self.door2 == 1:
                print("You win")
            else:
                print("You loose")
        elif self.choice == 3:
            if self.door3 == 1:
                print("You win")
            else:
                print("You loose")

g1 = Game()

print(g1.door1)
print(g1.door2)
print(g1.door3)


g1.make_choice(1)

g1.check_result()