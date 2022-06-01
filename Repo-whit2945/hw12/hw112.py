import tkinter as tk
import random

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    #print("Implement this and then remove this print statement")
    def __init__(self, name, dexNum, catchRate, speed):
        self.name = name
        self.dexNum = dexNum
        self.catchRate = catchRate
        self.speed = speed
    def __str__(self):
        return str(self.name)
    def get_dexNum(self):
        return str(self.dexNum)
    def get_catchRate(self):
        return str(self.catchRate)
    def get_speed(self):
        return str(self.speed)
    


#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        #print("In SafariSimulator init")
        self.count = 0
        self.pokepoke = [] #This list keeps track of the caught pokemon
        self.master = master
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity
        
        #Initialize any instance variables you want to keep track of
        self.ballsLeft = 30
        with open('pokedex.csv', 'r') as file:
            text = file.read()
        text2 = text.split(",")
        self.d = {}
        self.ls = []
        for i in range(4 ,len(text2)-1, 3):
            self.ls.append(text2[i])
            text3 = text2[i-1].split('\n')
            text4 = text2[i+2]
            if '\n' in text4:
                num = text2[i+2].index('\n')
                text5 = text4[:num]
                self.d[text2[i]] = Pokemon(text2[i], text3[1], text2[i+1], text5)
            else:
                self.d[text2[i]] = Pokemon(text2[i], text3[1], text2[i+1], text4)
        #DO NOT MODIFY: These lines set window parameters and create widgets

        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.pokeInfo = self.nextPokemon()
        self.poke = self.pokeInfo[0]
        self.Image = self.pokeInfo[1]
        print(self.poke)
        self.createWidgets()
        #Call nextPokemon() method here to initialize your first random pokemon

        
    def createWidgets(self):
        #print("In createWidgets")
        #See the image in the instructions for the general layout required
        #"Run Away" button has been completed for you as an example:
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack(side="bottom")
        
        #You need to create an additional "throwButton"
        self.throwButton = tk.Button(self)
        self.throwButton["text"] = "Throw Safari Ball (" + str(self.ballsLeft) + " left)"
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack(side="top")
        
        #A label for status messages has been completed for you as an example:
        self.messageLabel = tk.Label(bg="grey")
        self.messageLabel["text"] = "You encounter a wild " + self.poke.name
        self.messageLabel.pack(fill="x", padx=5, pady=5)

        #You need to create two additional labels:

        #Complete and pack the pokemonImageLabel here.        
        self.image = tk.Label(width=141, height=210)
        self.image.pack()
        self.image["image"] = self.Image
        self.image.pack()
        #Complete and pack the catchProbLabel here.
        p_catchR = int(self.poke.catchRate)
        num = min(p_catchR+1, 151)/449.5
        num *= 100
        n = int(num)
        self.catchProbLabel = tk.Label(bg="grey")
        self.catchProbLabel["text"] = "Your chance of catching it is " + str(n) + "%!"
        self.catchProbLabel.pack(fill="x", padx=5, pady=5, side = "bottom")

    def nextPokemon(self):
        #print("In nextPokemon")
        if self.count == 0:
            ls = []
            ls.append(self.d[random.choice(self.ls)])
            s = tk.PhotoImage(file="sprites/" + str(ls[0].dexNum) +".gif")
            ls.append(s)
            self.count += 1
            return ls
        else:
            self.poke = self.d[random.choice(self.ls)]
            self.Image = tk.PhotoImage(file="sprites/" + str(self.poke.dexNum) +".gif")
            self.image["image"] = self.Image
            p_catchR = int(self.poke.catchRate)
            num = min(p_catchR+1, 151)/449.5
            num *= 100
            n = int(num)
            self.messageLabel["text"] = "You encounter a wild " + self.poke.name
            self.catchProbLabel["text"] = "Your chance of catching it is " + str(n) + "%!"
            print(self.poke)
            
        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
        
    def throwBall(self):
        #print("In throwBall")
        self.ballsLeft -= 1
        self.throwButton["text"] = "Throw Safari Ball (" + str(self.ballsLeft) + " left)"
        #if self.ballsLeft == 0:
            #self.endAdventure()
        r = random.random()
        #print(r)
        m = min((int(self.poke.catchRate)+1), 151) / 449.5
        #print(m)
        if r < m:
            self.pokepoke.append(self.poke)
            self.nextPokemon()
        else:
            self.messageLabel["text"] = "Aargh! It escaped!"
        if self.ballsLeft == 0:
            self.endAdventure()
        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
        
    def endAdventure(self):
        #print("In endAdventure")
        s = ""
        self.messageLabel["text"] = "You're all out of balls, hope you had fun"
        self.runButton.pack_forget()
        self.throwButton.pack_forget()
        self.image.pack_forget()
        self.catchProbLabel.pack_forget()
        if len(self.pokepoke) == 0:
            s = "Oops you caught 0 Pokemon."
        else:
            s = "You caught " + str(len(self.pokepoke)) + " Pokemon\n"
            for i in self.pokepoke:
                s += i.name + '\n'
        self.end = tk.Label(bg="grey")
        self.end["text"] = s
        print(s)
        self.end.pack(fill="x", padx=5, pady=5)
        #This method must: 

            #Display adventure completion message
            #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.

#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
