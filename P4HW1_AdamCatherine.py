# CTI-110
# P4HW1 - Score List
# Catherine Adam 
# March 31, 2022
#
# Have user enter the number of scores they would like to enter.
# Make a loop to collect each of the scores the user enters.
# Ensure score is valid, if not prompt user to enter a valid score.
# Add valid scores to a list. Then calculate and print the lowest score entered,
# score list after dropping the lowest score, the average of the remaining
# scores, and the letter grade for said average.

scores_total = int(input('How many scores do you want to enter? '))
print()
i = 1
scores_list = []

while i <= scores_total:
    print('Enter score',f'#{i}: ',end='')
    score_entered = int(input())

    if score_entered <0 or score_entered >100:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        print('Enter score',f'#{i} again.')

    else:
        scores_list.append(score_entered)
        i += 1
        
scores_minimum = min(scores_list)

scores_list.remove(scores_minimum)

average_scores = (sum(scores_list)/len(scores_list))

if average_scores >= 90:
    letter_grade = 'A'

elif average_scores >=80:
    letter_grade = 'B'

elif average_scores >=70:
    letter_grade = 'C'

else:
    letter_grade = 'F'

print('--------------Results--------------')

print('Lowest Score  :', scores_minimum)

print('Modified List :', scores_list)

print('Scores Average:', f'{average_scores:.2f}')

print('Grade         :', letter_grade)

print('-----------------------------------')
