try:
   input = raw_input
except NameError:
   pass

import sys
from pickle import load
dict = load(open("dictCoursesPreCoReqs.p", "rb"))

print ("Welcome! This tool helps you find out which courses require the given course as a pre-req or co-req. I hope it is useful.")

def interaction():
	print ("")

	course_input = input("Which course would you like to look up? (Enter x to exit): ").upper()
	if (course_input != "X"):
		print("")
		pre_co_req_for = []

		if (not(course_input in dict)):
			print ("That is not a valid course")
			interaction()
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

