# CTI-110
# P2HW2 - Score Avg
# Catherine Adam 
# March 1, 2022
#
# Have the user enter 7 scores separately with individual statements created for each of the scores
# with floating point indentified.
# Each of the 7 score variables are placed into a list.
# The minimum value of the list is determined and given a variable. The variable is then printed
# into the Results section.
# The mimimum value variable is dropped from the list. The list is then printed next in the Results
# section, showing that the variable for minimum value has been removed.
# The average of the remaining scores is then calculated, by finding the sum of the 6 numbers left
# on the list and dividing that sum by 6. The average is printed last in the results section.


score_one = float(input('Enter score #1: '))
score_two = float(input('Enter score #2: '))
score_three = float(input('Enter score #3: '))
score_four = float(input('Enter score #4: '))
score_five = float(input('Enter score #5: '))
score_six = float(input('Enter score #6: '))
score_seven = float(input('Enter score #7: '))

scores_list = [score_one, score_two, score_three, score_four, score_five, score_six, score_seven]

scores_minimum = min(scores_list)

scores_list.remove(scores_minimum)

average_scores = (sum(scores_list)/6)



print('--------------Results--------------')

print('Lowest Score  :', scores_minimum)

print('Modified List :', scores_list)

print('Scores Average:', f'{average_scores:.2f}')

print('-----------------------------------')

