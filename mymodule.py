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
        self.doors[self.choice] = "*"

    def check_result(self):

        if self.tresor == self.choice:
            return 1
        else:
            return 0


    def remove_door(self):
        n = random.randint(0,2)
        while n == self.tresor or n == self.choice:            
            n = random.randint(0,2)
        self.rmdoor = n
        self.doors[self.rmdoor] = "X"
        
    def switch_choice(self):
        n = random.randint(0,2)
        while n == self.choice or n == self.rmdoor:
            n = random.randint(0,2)
        self.doors[self.choice] = "_"
        self.choice = n
        self.doors[self.choice] = "*"

# could be nice to have a print function
# to use like print(g1) but heh
    def __str__(self):
        return "[ " + ' , '.join(self.doors) + " ]"





