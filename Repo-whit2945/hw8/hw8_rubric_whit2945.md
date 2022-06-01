﻿# HW8 - CSCI 1133 - Rubric

 * Grader Name: **Name**
 * Grader email: **@umn.edu**
 * Homework Total: **40**
 * Grade: **37.5**

## General Deductions:

* Incorrectly named/submitted source file (-8)
* Constraints not followed (-40% PER PROBLEM)
* Failure to execute due to syntax errors (-30% PER PROBLEM)
* Bad Style

## get_data_list (10 pnts):

### Points Deducted: 0

* +1 Correct Function Definition
* +1 Correct Return Type 
* +2 Opened File Correctly
* +1 Reads from the file correctly
 * +1 Closes the file at the end
 * +2 Tests (+0.5 pt/each)

## hw8_index (10 pnts):

### Points Deducted: 0

* +1 Correct Function Definition
* +1 Correct Return Type 
* +8 Found the correct index
	* +8 Used the string method to find the position of the column
 * +8 Using a Loop
	 * +2 Used split to get a list of strings
	 * +4 Looped through the whole list to find homework 8
	 * +2 Found the correct index
	    * -1 Off-by one index.


## alter_grade (10 pnts):

### Points Deducted: 0

* +1 Correct Function Definition
* +1 Correct Return Type 
* +8 Correctly Modified the String
	* +2 Split on ' , '
	* +2 Modified the correct index
	* +2 Put a 40 at the index
	* +2 Join with ' , '

## haxx (10 pnts):

### Points Deducted: 2.5

* +1 Correct Function Definition
* +1 Correct Return Type 
* +2 Get the data from the file using get_data_list
* +1 Get the index from the data using hw8_index
  * **-0.5 does not return False if file does not contain hw8 grade column**
* +2 update with the altered string
* +1 Opened the file with "w" (For Writing)
* **+1 Correctly wrote back to the file**
* **+1 Closed the file**

## Grader Comment:

Nice job!