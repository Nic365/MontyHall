import random

class Game:
    def __init__(self):
        self.choice = None
        self.rmdoor = None
        self.tresor = random.randint(0,2)
        self.doors = ["_", "_", "_"]
        self.doors[self.tresor] = "$"

    def make_choice(self, choice):
        self.choice = choice

    def check_result(self):
        if self.doors[self.choice] == "$":
            return 1
        else:
            return 0


    def remove_door(self):
        n = random.randint(0,2)
        while n == self.tresor or n == self.choice:            
            n = random.randint(0,2)
        self.rmdoor = n
        self.doors[self.rmdoor] = "X"
        
    #def __str__(self):
        #return self.doors

# test

g1 = Game()
g1.make_choice(1)
print(g1.doors)
g1.remove_door()
print(g1.doors)
print(g1.check_result())

""" rounds = 1000

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
 """
#Percentage = 100 * float(part)/float(whole)


