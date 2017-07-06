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

	courseInput = input("Which course would you like to look up? ").upper()
	print("")
	preCoReqFor = []

	if (not(courseInput in dict)):
		print ("That is not a valid course")
		interaction()
	else:
		for course, preCoReqs in dict.items():
			if (courseInput in preCoReqs):
				preCoReqFor.append(course)

		sys.stdout.write(courseInput + " is a pre-req or co-req for:")
		print("")
		'''print(preCoReqFor)
		print("")'''
		preCoReqFor.sort()
		for p in preCoReqFor:
			sys.stdout.write("| " + str(p) + " |")
		print("")
		print("")

		doAgain = input("Would you like to look up another course?[yes/no] ").lower()
		if (doAgain == "yes"):
			interaction()

interaction()

