# Author: Chase Holt
# Section: CIS-225-01
# Date: 6/19/2019
# File: campus_gpa.py
#
# Today we are aiming for a gpa average for the student's on a given campus.


######################################################################
# Name: initialize
# Purpose: initializes all starting numbers to 0
# Input: none
# Output: returns sum, count, gpa
#######################################################################

def initialize():

	sum = 0
	
	count = 0
	
	gpa = 0
	
	return sum, count, gpa
	
######################################################################
# Name: gpa_processing
# Purpose: processes the campus gpa 
# Input: each student's gpa
# Output: sends the gpa gpa to display
#######################################################################

def gpa_processing():

	sum, count, gpa = initialize()
		
	
	while gpa >= 0:
		gpa = input("Enter your first gpa: ")
		try:
			gpa = float(gpa)
			if gpa < 0:
				break
			else:
				sum = sum + gpa
				print("Enter a negative number to stop or: ")
				count = count + 1
		except:
			gpa_processing()
	else:
		print("loop over")

	avg_gpa = sum / count
	
	return avg_gpa, count
	
######################################################################
# Name: display_gpa
# Purpose: displays our results
# Input: none
# Output: displays our average gpa and number of students on the console.
#######################################################################
		
def display_gpa():

	
	avg_gpa, count = gpa_processing()
	
	print("\n", "The average campus gpa is: ", '{:.2f}'.format(avg_gpa), "\n", "and the number of students surveyed is: ", count)
display_gpa()
