def input():
	msg = 'Would you like to input some test scores?'
	stillinputing = raw_input("%s (yes/no) " % msg)
	tablenames = []
	tablemark1 = []
	tablemark2 = []
	tablemark3 = []

	while stillinputing == 'yes':
		name = raw_input("What is the name of the student who's marks you would like to enter: ")
		mark1 = raw_input("What did this student get in the first computer science test: ")
		mark1 = eval(mark1)
		while mark1 > 20 or mark1 < 0:
			mark1 = raw_input("Please enter the mark out of 20: ")
			mark1 = eval(mark1)
			print mark1
		mark2 = raw_input("What did this student get in the second computer science test: ")
		mark2 = eval(mark2)
		while mark2 > 25 or mark2 < 0:
			mark2 = raw_input("Please enter the mark out of 25: ")
			mark2 = eval(mark2)
			print mark2
		mark3 = raw_input("What did this student get in the third computer science test: ")
		mark3 = eval(mark3)
		while mark3 > 35 or mark3 < 0:
			mark3 = raw_input("Please enter the mark out of 35: ")
			mark3 = eval(mark3)
			print mark3
		tablenames.append(name)
		tablemark1.append(mark1)
		tablemark2.append(mark2)
		tablemark3.append(mark3)
		print tablenames
		print tablemark1
		print tablemark2
		print tablemark3
	
input()