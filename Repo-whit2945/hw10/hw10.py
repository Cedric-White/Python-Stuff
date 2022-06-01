class Complex:
    #==========================================
    # Purpose: This function intiates the values used in my "Complex" class
    # Input Parameter(s): "real" represents the real component, and "imag"
    # represents the imaginary component. And the "self" parameter is used to
    # initialize objects
    # Return Value(s): This function returns nothing
    #==========================================

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    #==========================================
    # Purpose: This function returns the value of the real component.
    # Input Parameter(s): The "self" parameter is used here to retrieve the values
    # associated with a particular Complex instance's "real" component. 
    # Return Value(s): The value of the "real" complex component as a string. 
    #==========================================
    def get_real(self):
        return str(self.real)
    
    #==========================================
    # Purpose: This function returns the value of the imaginary component.
    # Input Parameter(s): The "self" parameter is used here to retrieve the values
    # associated with a particular Complex instance's "imag" component. 
    # Return Value(s): The value of the "imag" complex component as a string. 
    #==========================================
    def get_imag(self):
        return str(self.imag)
    
    #==========================================
    # Purpose: This function sets the real component to a new value.
    # Input Parameter(s): This funtion has the "self" parameter is used here to
    # set a new value from the value of "new_real"
    # Return Value(s): Nothing gets returned 
    #==========================================
    def set_real(self, new_real):
        self.real = new_real
        
    #==========================================
    # Purpose: This function sets the imaginary component to a new value.
    # Input Parameter(s): This funtion has the "self" parameter is used here to
    # set a new value from the value of "new_imag"
    # Return Value(s): Nothing gets returned 
    #==========================================
    def set_imag(self, new_imag):
        self.imag = new_imag
        
    #==========================================
    # Purpose: This fucntion returns the Complex number in a form that
    # complex numbers are read in. 
    # Input Parameter(s): The "self" parameter. This parameter is used to
    # retrieve the values of the two values associated with a given complex
    # object. 
    # Return Value(s): The complex number is returned in this format.
    # "<real> + <imag>i"
    #==========================================
    def __str__(self):
        return str(self.real) + ' + ' + str(self.imag) + 'i'

    #==========================================
    # Purpose: This function adds two Complex numbers together into a new
    # complex object
    # Input Parameter(s): The input parameters here are "self", and "other"
    # used here to retrieve data from two diffrent Complex objects for adding.
    # Return Value(s): A new Complex object contain the sum of two Complex objects
    # is returned
    #==========================================

    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)

    #==========================================
    # Purpose: This function multiplies two Complex numbers together into a new
    # complex object
    # Input Parameter(s): The input parameters here are "self", and "other"
    # used here to retrieve data from two diffrent Complex objects for multiplication.
    # Return Value(s): A new Complex object contain the product of two Complex objects
    # is returned.
    #==========================================

    def __mul__(self, other):
        return Complex((self.real*other.real)-(self.imag*other.imag),(self.real*other.imag)+(self.imag*other.real))

    #==========================================
    # Purpose: This function determines if two Complex objects are equal.
    # Input Parameter(s): The input parameters here are "self", and "other"
    # used here to retrieve data from two diffrent Complex objects to determine
    # if they are equal or not. 
    # Return Value(s): True is returned if they are equal, and False is returned
    # if they are not equal. 
    #==========================================

    def __eq__(self, other):
        if (self.real == other.real) and (self.imag == other.imag):
            return True
        else:
            return False

class Employee:
    #==========================================
    # Purpose: This function instantiates the five variables used in the rest
    # of the class; "name", "position", "salary", "seniority", and value.
    # Input Parameter(s): This function has the "self" parameter used here to
    # instantiate the variables from the "line" string.  
    # Return Value(s): Nothing get returned
    #==========================================

    def __init__(self, line):
        line2 = line.split(",")
        self.name = line2[0]
        self.position = line2[1]
        self.salary = line2[2]
        self.seniority = line2[3]
        self.value = line2[4][0:-1]
    #==========================================
    # Purpose: This function overwrites the print function so this class can
    # print fromated information about a specific Employee object. The given
    # format is: "<Name>, <Position>". 
    # Input Parameter(s): This function has the "self" parameter used here to
    # access the values of "name" and "position". 
    # Return Value(s): The values of "name" and "position" with the given format
    #==========================================

    def __str__(self):
        return self.name + ", " + self.position
    #==========================================
    # Purpose: This function returns the float values of the difference
    # between "value" and the "salary" of a given Employee object.
    # Input Parameter(s): This function has the "self" parameter used here to
    # access the values of "value" and "salary". 
    # Return Value(s): The difference of "value" and "salary" is returned. 
    #==========================================

    def net_value(self):
        return float(self.value)-float(self.salary)
    #==========================================
    # Purpose: This function determines if first object is less than the second
    # object. In other words, if the Employee object to the left is less than
    # the object to the left then True is returned, if not then False is returned.
    # Input Parameter(s): This function has the "self" parameter, and "other" parameters
    # used here to access to different Employees' "net_value".
    # Return Value(s): A boolean value is returned (True or False) 
    #==========================================
    def __lt__(self, other):
        if self.net_value() < other.net_value():
            return True
        else:
            return False
        
class Branch(Employee):
    #==========================================
    # Purpose: This fucntion initializes the Branch object.
    # Input Parameter(s): This function has the "self" parameter, used here
    # to initialize variables of the Branch class. And the "name" parameter
    # that is the string for file name.
    # Return Value(s): This function returns nothing.
    #==========================================
    def __init__(self, name):
        self.name = name
        with open(self.name, 'r') as file:
            text = file.read()
        text2 = text.split(",")
        self.location = text2[1]
        self.upkeep = text2[5]
        self.team = []
        self.nums = 0
        for i in range(12,len(text2), 4):
            s = text2[i]
            s2 = s.split('\n')
            self.team.append(s2[1])
        self.team = self.team[:-1]
    #==========================================
    # Purpose: This function overwrites the print function so this class
    # can print the desired representation of a Branch object.
    # Input Parameter(s): This function has the "self" parameter, used here
    # to access the variables of the Branch class
    # Return Value(s): A string representing the desired representation
    # of a Branch object is returned.
    #==========================================
    def __str__(self):
        try:
            string = str(self.location)
            string += '\n'
            with open(self.name, 'r') as file:
                text = file.read()
            text2 = text.split(",")
            ls = []
            for i in range(13,len(text2), 4):
                ls.append(text2[i])
            for i in range(len(self.team)):
                string += self.team[i]
                string += ', '
                string += ls[i]
                string += '\n'
        except IndexError:
            s = self.location + '\n'
            string = s + self.team
            self.team = string
            self.name = ''
        return string
    #==========================================
    # Purpose: This funtion takes in no arguments (other than self),
    # and returns the sum of the net values of all of the employees in
    # the branch, minus the upkeep of the branch.

    # Input Parameter(s): This function only has the "self" input parameter
    # used here to access values from the Branch object
    # Return Value(s): This function returns the difference of the sum of all
    # the branches and the upkeep.
    #==========================================
    def profit(self):
        num = 0
        try:
            with open(self.name, 'r') as file:
                text = file.readlines()
            for i in range(3, len(text)):
                e = Employee(text[i])
                num += e.net_value()
            num -= float(self.upkeep)
        except FileNotFoundError:
            num = self.nums
            num -= float(self.upkeep)
        return num
    #==========================================
    # Purpose: This function overloads the "less than" operator. So we can use
    # it with Branch objects as we choose.
    # Input Parameter(s): This function has the "self" parameter, and "other" parameters
    # used here to access to different Employees' "profit".
    # Return Value(s): A boolean value is returned.
    #==========================================
    def __lt__(self, other):
        if self.profit() < other.profit():
            return True
        else:
            return False
    #==========================================
    # Purpose: (What does the function do?)
    # Input Parameter(s): This function has the input two input parameters; "self"
    # and "num". "self" is used to access variables from the Branch Class.
    # "num" is the int value for how many employees are cut.
    # Return Value(s): A string with the remaining employees is returned. 
    #==========================================
    def cut(self, num):
        self.num = num
        ls = []
        s = ""
        with open(self.name, 'r') as file:
            text = file.readlines()
        for i in range(3, len(text)):
            e = Employee(text[i])
            ls.append(e)
        ls2 = sorted(ls)
        for i in range(num):
            del ls2[0]
        for i in range(len(ls2)):
            self.nums+=ls2[i].net_value()
            s += str(ls2[i])
            s += '\n'
        self.team = s
        return s
    
class Company(Branch):
    #==========================================
    # Purpose: This fucntion initializes the Company object.
    # Input Parameter(s): This function has the "self" parameter, used here
    # to initialize variables of the Company class. And the "name" parameter
    # that is the string for file name. And the "branches" parameter for the
    # list of branch obejects
    # Return Value(s): This function returns nothing.
    #==========================================
    def __init__(self, name, branches):
        self.name = name
        self.branches = branches
        
    #==========================================
    # Purpose: This function overwrites the print function so this class
    # can print the desired representation of a Company object.
    # Input Parameter(s): This function has the "self" parameter, used here
    # to access the variables of the Company class
    # Return Value(s): A string representing the desired representation
    # of a Company object is returned.
    #==========================================
    def __str__(self):
        string = ''
        for i in self.branches:
            string += i
        return string 
    #==========================================
    # Purpose: This function finds the branch with the lowest profit margin
    # and cut half (rounded down) of the employees from that branch
    # Input Parameter(s): The only input parameter this function has is "self"
    # used here to access Company class values.
    # Return Value(s): Nothing is returned
    #==========================================
    def synergize(self):
        pass
