# Fix and create a program that will calculate students grades.
# March 19th 2022
# CTI-110 P2HW1 - Debugging
# Catherine Adam
#
# This program takes a number grade and outputs a letter grade.
# The system uses 10-point grading scale.
# There are 5 letter grades. Four are defined and anything else falls under the
# remaining range.

def main():
    
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
 
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: B')
    else:
        print('Your grade is: F')

main()
