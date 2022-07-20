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
                return 1
            else:
                return 0
        elif self.choice == 2:
            if self.door2 == 1:
                return 1
            else:
                return 0
        elif self.choice == 3:
            if self.door3 == 1:
                return 1
            else:
                return 0


    def remove_door(self):
        None
        # retirer une porte qui n'est pas le tresor ni celle choisit
        #  comment ?


# test

rounds = 1000

print("No change rounds")
win, lost = 0, 0
for i in range(1, rounds):
    g1 = Game()
    #print(g1.door1, g1.door2, g1.door3)
    g1.make_choice(1)
    g1.remove_door()

    if g1.check_result():
        win+=1
    else:
        lost+=1

print("Win:", win)
print("lost:", lost)
print(round(100 * win/(win+lost),2),"%")

#Percentage = 100 * float(part)/float(whole)


