#==========================================
# Purpose: The purpose of function "length_contract" is
# is to calculate Relativistic Length Contraction
# Input Parameter(s): This function has two parameters, dist
# and speed, and they are used to calculate contracted length.
# "dist" represents the distance inbetween two points in meters, and "speed"
# represents the speed that an object or spaceship is traveling
# in meters/second. 
# Return Value(s): This function returns the contracted length after the
# two variables, dist and speed, are plugged into the equation given to us.
#==========================================
def length_contract(dist, speed):
     return dist*(1 - (speed**2/300000000**2))**0.5
#==========================================
# Purpose: The purpose of this function is to calculate and print
# the time required to traverse the segment, as seen by a stationary observer,
# in years. Also to return the contracted length as calculated by a call to the
# "length_contract" function explained above.
# Input Parameter(s): This function has 1 parameter "speed" and three variables
# "parsec_twelve", "year", and "time".
# "speed" is just speed of the moving spaceship. 
# "parsec_twelve" is 12 parsecs converted to meters.
# "year" is just the amount of seconds in a year. "time" just stores the amount
# of years need required to traverse the distance, as seen by a stationary
# observer. 
# Return Value(s): A call to the length_contract(dist, speed) gets returned
# So the only thing that gets returned is the calculated
# Relativistic Length Contraction
#==========================================
def  bessel_run(speed):
     parsec_twelve = 30860000000000000 * 12
     year = 31557600
     time = (parsec_twelve/speed)/year
     print(time)
     return length_contract(time ,speed)
#==========================================
# Purpose: This function calls the print function 5 times to print
# "Who needs loops?"
# Input Parameter(s): This function doesn't take any parameters or
# uses any variables
# Return Value(s): This function does not return anything. It only prints
# "Who needs loops?" 
#==========================================
def who_needs_loops():
     print("Who needs loops?")
     print("Who needs loops?")
     print("Who needs loops?") 
     print("Who needs loops?") 
     print("Who needs loops?")
#==========================================
# Purpose: This function calls the "who_needs_loops" function 5 times
# thereby printing "Who needs loops" 25 times.
# Input Parameter(s): This function doesn't take any parameters or
# uses any variables
# Return Value(s): This function does not return anything.
# it only calls other functions.
#==========================================
def number_of_prints():
     who_needs_loops()
     who_needs_loops()
     who_needs_loops()
     who_needs_loops()
     who_needs_loops()
#==========================================
# Purpose: This function calls a function called "calls number_of_prints()"
# 4 time to print "Who needs loops?" a hundred times
# Input Parameter(s): This function doesn't take any parameters or
# uses any variables
# Return Value(s): This function does not return anything.
# it only calls other functions.
#==========================================
def print_100():
     number_of_prints()
     number_of_prints()
     number_of_prints()
     number_of_prints()
