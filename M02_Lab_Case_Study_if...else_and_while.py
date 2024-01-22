#Pirince Liyo
# M02 Lab Case Study if else and while
# This Python app will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.
# DEAN_LIST is the variable that save my GPA in float, QUIT is a variable that save the string ZZZ, 
#last_name is a variabe that save the last name of the student entered
# first_name is a variabe that save the first name of the student entered
#gpa is the variable that entered value of GPA
DEAN_LIST = 3.5
QUIT = 'ZZZ'

last_name = input(f'Enter Student Last Name or {QUIT} to QUIT: ')
while last_name != QUIT:
    first_name = input(f'Enter Student First Name: ')
    gpa = input('Enter Student GPA: ')
    if float(gpa) >= DEAN_LIST:
        print(f'{first_name} {last_name} has made the Deans List.')
        break
    else:
        print(f'{first_name} {last_name} has made the Honor Roll.')
        break
print('Done')
