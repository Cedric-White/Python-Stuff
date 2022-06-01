#==========================================
# Purpose: The purpose of this function is to return a string that represents
# a sound produced by a dog depending its weight. 
# Input Parameter(s): There is one input parameter called "weight".
# This input parameter represents the weight of a dog. 
# Return Value(s): There are four options for what this function can return and
# they all depend on the "weight" input parameter. If "weight" is less then 13,
# then 'Yip' is returned. If "weight" is greater than 13, but less than or eqaul
# to 30, then 'Ruff' is returned. If "weight" is greater than 30, but less than
# 70, then 'Bark' is returned. Lastly, if "weight" is higher than 70, then
# 'Boof' is returned. 
#==========================================
def sound(weight):
    if weight < 13:
        return 'Yip'
    elif weight <= 30:
        return 'Ruff'
    elif weight <= 70:
        return 'Bark'
    else:
        return 'Boof'

#==========================================
# Purpose: This function takes four strings from the user in order to
# simulate a mini text adventure interactive fiction game. In this game, the
# user has three options. To choose one of the three options the user
# enters 1,2, or 3. Any other input is ruled invalid and this
# function will continue to ask for a new input until it gets a valid answer. 
# Input Parameter(s): This function has four input parameters, "text","option1",
# "option2", and "option3". These parameters take in four strings and simulate
# the game by being printed out in a certain order for option selection. 
# Return Value(s): This function returns a variable that I created called
# "number". This variable only exists to cast the user input into a string and
# to return that string.
#==========================================
def choice(text,option1,option2,option3):
    print(text)
    print()
    print("1. ", option1)
    print("2. ", option2)
    print("3. ", option3)
    number = str(input("Choose 1, 2, or 3: "))
    while (number != '1') and (number != '2') and (number != '3'):
        print("Invalid option")
        number = str(input("Choose 1, 2, or 3: "))
    return number

#==========================================
# Purpose: The function takes the user on adventure by calling the choice() function multiple times
# Input Parameter(s): There are no input parameters. Only "answer(n)" variables (n = 1-6). That store the
# the user input.
# Return Value(s): Depending on the path of inputs, the user will eventually end up with a returned True or False.
#==========================================
def adventure():
    print("The time is 7:30 PM on a Wednesday")
    answer1 = choice("Goal: Get homework done and get to bed on time",
           "Grab phone and watch a minecraft livestream",
           "Throw phone into a blender",
           "Put phone in a timed safe with a emergency pin set by a friend")
    if answer1 == '1':
        print()
        print("You failed the quest. You are weak. Slept at 4 am.")
        return False
    if answer1 == '2':
        print()
        answer2 = choice("Breaking your immediate connection with your phone is important",
               "Plug in all the appliances in you kitchen into one power block, plugging the blender in last",
               "Try to plug the blender into your laptop",
               "Ask your friend to plug in the appliances like in option 1")
        if answer2 == '1':
            print()
            print("Surprisingly your phone survived. Probably because you took out the power for your room by shorting out your fuse box")
            print("Your wifi was shut off. Thankfully your profesors are still back in the stone ages and only assign paperwork.")
            print("Good job you were able to complete your homework!")
            return True
        if answer2 == '2':
            print()
            print("Plugging in your blender into you laptop didn't quite work out and or you chose alex")
            answer3 = choice("What's in it for alex?", "You give alex the dollar on your desk to choose a pin", "You plan to send him a buck on cash app",
                "You get mad at alex for requesting payment for such little of a favor and kick him out")
            if answer3 == '1':
                print()
                print("Good job you were able to complete your homework!")
                return True
            if answer2 == '3':
                print()
                answer3 = choice("Choose a friend that will choose the pin on the safe",
                "Choose Satan", "Choose Alex", "Choose David")
                if answer3 == '1':
                    print()
                    print("Why the hell did you choose Satan?!")
                    print("You have to sell your soul to get your phone back")
                    print("You completed the mission, but at what cost?")
                    return False
    if answer1 == '3':
        print()
        answer3 = choice("Choose a friend that will choose the pin on the safe",
                "Choose Satan", "Choose Alex", "Choose David")
        if answer3 == '1':
            print()
            print("Why the hell did you choose Satan?!")
            print("You have to sell your soul to get your phone back")
            print("You completed the mission, but at what cost?")
            return False
    if (answer3 == '2'):
        print()
        print("Plugging in your blender into you laptop didn't quite work out and or you chose alex")
        answer4 = choice("What's in it for alex?", "You give alex the dollar on your desk to choose a pin", "You plan to send him a buck on cash app",
                "You get mad at alex for requesting payment for such little of a favor and kick him out")
        if answer4 == '1':
            print()
            print("Good job you were able to complete your homework!")
            return True
        if answer4 == '3':
            print()
            print("Dude, he's broke and he can see the dollar on your table.")
            print("You failed the quest. You are weak. Slept at 4 am.")
            return False
    if (answer4 == '2') or (answer3 == '3'):
        print()
        print("This is the final test")
        answer5 = choice("For this test, we going back in time.", "Earlier in the day you avoided buying a water costing a dollar",
               "You cash apped a homeless guy a buck", "You didn't give that homeless guy the dollar he so badly needed. Shame!")
        if (answer5 == '1') or (answer5 == '3'):
            print()
            print("Wow, you were able to finish you homework and go to sleep at time, but you are either thirsty or very selfish.")
            return True
        if answer5 == '2':
            print()
            print("You were able to finish your homework, but alex didn't get his money and he won't give you the combo for the safe.")
            print("The one time being charitable resulted in bad karma")
            return False
