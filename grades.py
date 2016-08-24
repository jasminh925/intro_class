def convert_score_to_letter(score):
	#write conditionals that convert score number to letter
	#returns a letter based on each conditional
	for grade in score:
		grade = int(grade)
		if grade >= 90:
			print "%i is an A." % (grade)
		elif grade >= 80 and grade <= 89:
			print "%i is a B." % (grade)
		elif grade >= 70 and grade <= 79:
			print "%i is a C." % (grade)
		elif grade >= 60 and grade <= 69:
			print "%i is a D." % (grade)
		else:
			print "%i is an F." % (grade)


def process_file_to_list(grades_file):
	#open the file
	#read the file into a list
	#return the list
    with open(grades_file) as my_file:
        output_list = my_file.readlines()
    return output_list



def main():
	#call function to process file and save the list to variable
	#iterate through the list and convert the score to letter
	#print the score and the letter it converts to
	score = process_file_to_list("class_grades.txt")

	convert_score_to_letter(score)

if __name__ == '__main__':
   main()