# HW7 - CSCI 1133 - Rubric

 * Grader Name: **Grace Zenzen**
 * Grader email: **zenze007@umn.edu**
 * Homework Total: **40**
 * Grade: **0**

## General Deductions: Your file is blank.

* Incorrectly named/submitted source file (-8)
* Constraints not followed (-40% PER PROBLEM)
* Failure to execute due to syntax errors (-30% PER PROBLEM)
* Non-Recursive Solution (-100% PER PROBLEM, EXCLUDING PROBLEM C)

## Problem A - Collatz (10 pnts):

### Points Deducted: 

* +2 Base Case:
  * +1 Includes a Base case
  * +1 Correct Base Case
* +1 Correct Function Definition
* +1 Correct Return Type 
* +4 Correct Reduction Steps
  * +2 First Reduction Step
  * +2 Second Reduction Step
* +2 Test Cases (0.5 points each)
  * collatz(5) : [5, 16, 8, 4, 2, 1] 
  * collatz(12) : [12, 6, 3, 10, 5, 16, 8, 4, 2, 1] 
  * collatz(26) : [26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1] 
  * collatz(21) : [21, 64, 32, 16, 8, 4, 2, 1] 


## Problem B - Find_min (10 pnts):

### Points Deducted: 

* +1 if function name/parameters are correct
* +1 Return type is correct.
* +2 Base case is correct
* +4 Reduction Steps
  * +2 First Reduction Step
  * +2 Second Reduction Step 
* +2 Test Cases (0.5 points each)
  * find_min([100]) : 100
  * find_min([-10, -8, -12, 3])  : -12
  * find_min([-80, -81]) : -81
  * find_min([1, 2, 3, 4, 1]) : 1

## Problem C - Force_Win / Tic_tac_toe (20 pnts):

### Force_win (10 points)

#### Points Deducted: 

* +3 Base Cases:
  * +2 Has Base Cases
  * +1 Correct Base Cases
* +7 Reduction Step:
  * +2 Loop to check each move + Recursive Call to force_win 
  * +1 Calls open_slots to get moves for the player
  * +2 Returns the correct board result
  * +2 correctly finds the max and the min for X and O

### Tic_tac_toe (5 Points)

#### Points Deducted: 

* +1 Random Choice for X
* +4 Correct Loop To Choose Space for O:
  * +2 Force_win call
  * +2 Track which was the best move

### Test Cases (5 Points)

#### Points Deducted: 

* +0.5 force_win(['-', 'X', '-', 'O', 'X', '-', 'O', 'X', '-']) : 1
* +0.5 force_win(['O', 'X', '-', 'X', 'O', '-', '-', 'X', 'O']) : -1
* +0.5 force_win(['-', '-', '-', '-', 'X', '-', '-', '-', '-']) : 0
* +0.5 force_win(['X', '-', 'X', 'X', 'O', 'O', '-', '-', '-']) : 1
* +0.5 force_win(['-', 'X', '-', 'O', 'O', '-', 'O', 'X', 'X']) : -1
* +0.5 force_win(['O', 'X', '-', 'O', 'X', 'O', 'X', 'O', 'X']) : 1
* +0.5 force_win(['-', 'X', '-', 'O', 'X', '-', '-', 'O', '-']) : 1
* +1.5 play_games(5)
  * X wins 0
  * O wins (any number between 0-5)
  * Draws (any number between 0-5)

## Grader Comment:
Your file is blank, there were no points awarded.
