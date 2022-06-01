# HW10 - CSCI1133 Rubric

 * Grader Name: **Dylan Bauer**
 * Grader email: **bauer898@umn.edu**
 * Homework Total: **40**
 * Grade: **27

## General Deductions

* Incorrectly named/submitted source file, functions, or classes (20% per problem) 
* Constraints not followed (40% per problem) 
* Failure to execute due to syntax errors (30% per problem)
* Bad Style/Missing function templates (10% per problem)

## Complex Class (10 pts) :

### Points deducted : 

* +1 __ init __
  * Has self.real
  * Has self.imag
* +1 (1/2 pt each) getters
* +1 (1/2 pt each) setters
* +2 __ str __ 
  * +1 Correctly formats string
  * +1 Returns a string
* +2 __ mul __
  * +1 follows formula
  * +1 returns new object with new values
* +2 __ add __
  * +1 follows formula
  * +1 returns new object with new values
* +1 __ eq __
  * +0.5 Checks individual components for equality
  * +0.5 returns True/False

## Employee (10 pts) :

### Points deducted: 

* +4 __ init __
  * +1 parses string parameter
  * +2.5 (0.5 pt each) correct parameters
* +2 __ str __
  * +1 correctly formats string
  * +1 returns a string
* +2 net_value
  * +1 correct order (self.value - self.salary)
  * +1 returns correct int
* +2 __ lt __
  * +0.5 correct order (self < other)
  * +0.5 return True/False
  * +1 correctly checks components of both

## Branch (10 pts)

### Points deducted:

* +5 __ init __
  * +1 open/close file (for reading)
  * +0.5 self.location
  * +0.5 self.upkeep
  * +3 self.team
    * +1 self.team is a list
    * +1 correctly parses file
    * +1 calls Employee constructor for each member of the list
* +1 __ str __
  * +0.5 correctly formats strings
  * +0.5 returns a string
* +1 profit
  * +1 loops over the entire branch and sums based on individual employee net values
* +1 __ lt __
  * +0.5 correct order of comparison (self < other)
  * +0.5 return True/False
* +2 cut
  * +1 sorts
  * +1 removes lowest

## Company (10 pts) 

### Points deducted:

- +2 __ init __
  - +1 self.name
  - +1 self.branches
- +3 __ str __
  - +1 correctly formats name
  - +1 correctly formats branches
  - +1 correctly formats newlines
- +5 synergize
  - +1 sorts branches
  - +1 grabs lowest branch
  - +1 gets length of lowest branch
  - +1 rounds down half of lowest branch
  - +1 calls branch's cut function

## Grader Comments
Complex getters shouldn't type cast info to a string (-1)
Employee did not cast salary, seniority, and value to float (-1.5)
String method in Company does not format correctly (-3)
Synergize unimplemented (-5)
Upkeep not float (-0.5)
Did not make Employee objects in Branch (-1)
Company does not inherit from Branch (-0.5)
Branch str does not work as it was described (-0.5)
- you should not need to reopen the file
