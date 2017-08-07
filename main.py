try:
   input = raw_input
except NameError:
   pass

import sys
from pickle import load
# Load dictionary with courses and their pre-requisites and co-requisites
dict = load(open("dictCoursesPreCoReqs.p", "rb"))

print ("Welcome! This tool helps you find out which courses require the given course as a pre-req or co-req. I hope it is useful.")

def interaction():
	print ("")

	course_input = input("Which course would you like to look up? (Enter x to exit): ").upper()
	if (course_input != "X"):
		print("")
		pre_co_req_for = []

		# If the course that the user provided is not in the loaded dictionary, ask again
		if (not(course_input in dict)):
			print ("That is not a valid course")
			interaction()
		# Else, search the courses for which the provided course is a pre-requisite or co-requisite 
		# and add them to a list.
		else:
			for course, pre_co_reqs in dict.items():
				if (course_input in pre_co_reqs):
					pre_co_req_for.append(course)

			sys.stdout.write(course_input + " is a pre-req or co-req for:")
			print("")
			
			pre_co_req_for.sort()
			for p in pre_co_req_for:
				sys.stdout.write("| " + str(p) + " |")
			print("")
			print("")

			interaction()

interaction()

