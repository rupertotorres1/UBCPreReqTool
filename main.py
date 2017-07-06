from pickle import load
dict = load(open("dictCoursesPreCoReqs.p", "rb"), encoding="utf-8")

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

		print(courseInput, "is a pre-req or co-req for:")
		print(preCoReqFor)
		print("")

		doAgain = input("Would you like to look up another course?[yes/no] ").lower()
		if (doAgain == "yes"):
			interaction()

interaction()

