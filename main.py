# CONSTANTS
class options(object):
    maxscore = 40       # MAX possible score in the test
    numstudents = 0     # Set to 0 to enable continued input until stopped

# 'Student' Class
class Student:
    def __init__(self, name, gender, score, percent = 0):
        self.name = name.title()
        self.gender = gender.lower()
        self.score = score
        self.percent = round((score / options.maxscore)*100, 2)

# Key for sorting the array so output files in order
def sort_key(student):
    return student.percent

students = []   # Array for storing student objects

print("\n** NOTE: Enter 'Name: *' to end")

count = 0
while True:     # Infinite loop until exited
    count+=1    # increment count

    print("-----[ Student {} ]-----".format(count))

    name = ''
    while len(name) < 1:
        name = input("Name: ")
    if name == '*':
        break


    while True:     # infinitely loops until a valid gender is entered
        gender = input("Gender <m/f>: ").lower()
        if gender not in ['m', 'f']:
            print("ERROR: gender should be 'm' or 'f'")
        else:
            break   # exit loop since valid gender entered

    while True:     # infinitely loops until a valid score is entered
        try:        # try;except used to ensure program doesn't crash if non-int value entered
            score = int(input('Score: '))
        except ValueError:
            score = None    # reset score variable
            print("ERROR: score must be an integer")
        else:
            if score not in range(options.maxscore+1):      # if score not between 0 andthe max score (40)
                print("ERROR: score must be in range (0,{})".format(options.maxscore))
                score = None    # reset score variable
            else:
                break       # exit loop since score entered is valid


    students.append(Student(name,gender,score))     # add a Student object to the array of students with the entered values

    if count == options.numstudents and options.numstudents != 0:
        break       # if count has looped number of students times, and unlimited students not enabled


students = sorted(students, key=sort_key, reverse=True)     # sort students array into order of percentages

file = {'passed': open('passed.txt', 'w'), 'failed': open('failed.txt', 'w')}   # create the file objects

passCount = {'m': 0, 'f': 0}    # defining vars for storing pass counts
failCount = {'m': 0, 'f': 0}    # " for fail counts

for student in students:        # loop through all stored students
    if student.percent >= 60:   # if the student got higher than 60%
        file['passed'].write(student.name + ' : ' + student.gender + ' : ' + str(student.percent) + '%\n')
        passCount[student.gender] += 1      # increment the passed count of the students gender
    else:       # student got less than 60%
        file['failed'].write(student.name + ' : ' + student.gender + ' : ' + str(student.percent) + '%\n')
        failCount[student.gender] += 1      # increment the failed count of the students gender

file['passed'].write("\n" + "Males - {}".format(passCount['m']))
file['passed'].write("\n" + "Females - {}".format(passCount['f']))
file['failed'].write("\n" + "Males - {}".format(failCount['m']))
file['failed'].write("\n" + "Females - {}".format(failCount['f']))

file['passed'].close()
file['failed'].close()
