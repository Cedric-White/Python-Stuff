class Adventurer:
    #==========================================
    # Purpose: This function's purpose is to initialize class variables. 
    # Input Parameter(s): This function has 5 input parameters; "name",
    # "level", "strength", "speed", and "power".
    # Return Value(s): This function returns nothing 
    #==========================================
    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = self.level*6
        self.hidden = False

    #==========================================
    # Purpose: This function returns a string representing an
    # Adventurer object. 
    # Input Parameter(s): This fuction's only input parameter is
    # self. Used here to retrieve class variable data.
    # Return Value(s): This fuction returns a string representing
    # an Adventurer object. 
    #==========================================
    def __repr__(self):
        return str(self.name) + " - HP: " + str(self.HP)

    #==========================================
    # Purpose: This function returns a string depicting
    # an attack between two Adventurer objects.
    # Input Parameter(s): This function has two input parameters
    # "self" and "target". These input parameters access class data
    # from two different objects. 
    # Return Value(s): A string representing an attack is return
    #==========================================
    def attack(self, target):
        if target.hidden == True:
            return str(self.name) + " can't see " + str(target.name)
        else:
            a = self.strength + 4
            target.HP -= a
            return str(self.name) + ' attacks ' + str(target.name) + ' for ' + str(a) + ' damage'

    #==========================================
    # Purpose: This function determines if the first object is less than the second
    # object. In other words, if the Adventurer object to the left is less than
    # the object to the left then True is returned, if not then False is returned.
    # Input Parameter(s): This function has the "self" parameter, and "other" parameters
    # used here to access to different Adventurers' "HP".
    # Return Value(s): A boolean value is returned (True or False) 
    #==========================================
    def __lt__(self, target):
        if self.HP < target.HP:
            return True
        else:
            return False
        
class Fighter(Adventurer):
    #==========================================
    # Purpose: This function's purpose is to initialize class variables. 
    # Input Parameter(s): This function has 5 input parameters; "name",
    # "level", "strength", "speed", and "power".
    # Return Value(s): This function returns nothing 
    #==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level*12

    #==========================================
    # Purpose: This function returns a string depicting
    # an attack with a Fighter
    # Input Parameter(s): This function has two input parameters
    # "self" and "target". These input parameters access class data
    # from two different objects. 
    # Return Value(s): A string representing an attack is return
    #==========================================
    def attack(self, target):
        if target.hidden == True:
            return str(self.name) + " can't see " + str(target.name)
        else:
            a = (2*self.strength) + 6
            target.HP -= a
            return str(self.name) + ' attacks ' + str(target.name) + ' for ' + str(a) + ' damage'

class Thief(Adventurer):
    #==========================================
    # Purpose: This function's purpose is to initialize class variables. 
    # Input Parameter(s): This function has 5 input parameters; "name",
    # "level", "strength", "speed", and "power".
    # Return Value(s): This function returns nothing 
    #==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level*8
        self.hidden = True
        
    #==========================================
    # Purpose: This function returns a string depicting
    # an attack with a Thief
    # Input Parameter(s): This function has two input parameters
    # "self" and "target". These input parameters access class data
    # from two different objects. 
    # Return Value(s): A string representing an attack is return
    #==========================================
    def attack(self, target):
        if self.hidden == False:
            return (Adventurer.attack(self, target))
        else:
            if (target.hidden == True) and (self.speed < target.speed):
                return str(self.name) + " can't see " + str(target.name)
            else:
                a = (self.level+self.speed)*5
                target.HP -= a
                self.hidden = False
                target.hidden = False
                return str(self.name) + ' sneak attacks ' + str(target.name) + ' for ' + str(a) + ' damage'

class Wizard(Adventurer):
    #==========================================
    # Purpose: This function's purpose is to initialize class variables. 
    # Input Parameter(s): This function has 5 input parameters; "name",
    # "level", "strength", "speed", and "power".
    # Return Value(s): This function returns nothing 
    #==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.fireballs_left = self.power

    #==========================================
    # Purpose: This function returns a string depicting
    # an attack with a Wizard
    # Input Parameter(s): This function has two input parameters
    # "self" and "target". These input parameters access class data
    # from two different objects. 
    # Return Value(s): A string representing an attack is return
    #==========================================
    def attack(self, target):
        if self.fireballs_left == 0:
            return (Adventurer.attack(self, target))
        else:
            target.hidden = False
            a = self.level*3
            self.fireballs_left -= 1
            target.HP -= a
            return str(self.name) + ' casts fireball on ' + str(target.name) + ' for ' + str(a) + ' damage'
        
#==========================================
# Purpose: This function puts two Adventurer objects, and or
# one of the child classes face to face in a duel.  
# Input Parameter(s): This function has two input parameters
# "adv1" and "adv2". These are two Adventurer objects or one of the
# child class objects. 
# Return Value(s): This function returns True or False
# depending on the outcome of the duel
#==========================================
def duel(adv1, adv2):
    print(adv1)
    print(adv2)
    if (adv1.HP <= 0) and (adv2.HP <= 0):
        print("Everyone loses!")
        return False
    if adv1.HP <= 0:
        s = str(adv2.name) + " wins!"
        print(s)
        return False
    if adv2.HP <= 0:
        s = str(adv1.name) + " wins!"
        print(s)
        return True
    while(adv1.HP > 0) and (adv2.HP > 0):
        print(adv1.attack(adv2))
        if adv2.HP <= 0:
            if (adv1.HP <= 0) and (adv2.HP <= 0):
                print("Everyone loses!")
                return False
            s = str(adv1.name) + " wins!"
            print(adv1)
            print(adv2)
            print(s)
            return True
        print(adv2.attack(adv1))
        print(adv1)
        print(adv2)
        if adv1.HP <= 0:
            if (adv1.HP <= 0) and (adv2.HP <= 0):
                print("Everyone loses!")
                return False
            s = str(adv2.name) + " wins!"
            print(s)
            return False
        
#==========================================
# Purpose: This function's purpose is to put a list
# of Adventurer's against each in a series of duels.
# Input Parameter(s): This function has only one input parameter
# "adv_list" which is a list of Adventurer objects.
# Return Value(s): An Adventurer object is returned.
#==========================================
def tournament(adv_list):
    if len(adv_list) == 0:
        return None
    if len(adv_list) == 1:
        return adv_list[0]
    ls = sorted(adv_list)
    while(len(ls) > 1):
        duel(ls[-2],ls[-1])
        ls = sorted(ls)
        for i in ls:
            if i.HP <= 0:
                ls.remove(i)
    return ls[0] 
        
    
