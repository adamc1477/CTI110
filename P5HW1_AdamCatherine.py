# CTI-110
# P5HW1 - Score List
# Catherine Adam 
# April 29, 2022
#
# Have user enter the number of scores they would like to enter.
# Make a loop to collect each of the scores the user enters.
# Ensure score is valid, if not prompt user to enter a valid score.
# Add valid scores to a list. Then calculate and print the lowest score entered,
# score list after dropping the lowest score, the average of the remaining
# scores, and the letter grade for said average.
# Create a menu with 3 options, create a list to make a list, display results to
# give your calculated results, and quit option to exit the program.
def main():
    def scores_list_total(): #function 1, create scores list
        scores_total= int(input('How many scores do you want to enter? '))
        i = 1
        global scores_list
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

        return scores_list

    def calculated_results(): #function 2, calculate results
        minimum_score =  min(scores_list)   
        scores_list.remove(min(scores_list))
        average_scores = (sum(scores_list)/len(scores_list))

        if average_scores >= 90:
            letter_grade = 'A'
        elif average_scores >=80:
            letter_grade = 'B'
        elif average_scores >=70:
            letter_grade = 'C'
        elif average_scores >=60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        print('--------------Results--------------')
        print('Lowest Score  :', minimum_score)
        print('Modified List :', scores_list)
        print('Scores Average:', f'{average_scores:.2f}')
        print('Grade         :', letter_grade)
        print('-----------------------------------')
        print()

    menu_selection = True
    while menu_selection:
        print ('-----------MENU-------------')
        print('1) Create Score List')
        print('2) Display Results')
        print('3) Exit')
        print('----------------------------------')
        print()
        menu_selection = int(input('Enter choice: ')) 
        if menu_selection == 1:
            scores_list_total() #creates list
        elif menu_selection == 2:
            if len(scores_list) == 0:
                print('Created list first')
                main()
            else:
                calculated_results()#displays the results
                
        elif menu_selection == 3:
            break #ends the program
        else:
            print()
            print('INVALID choice entered !!!!!')
            print('Choose from menu options please')
            print()
            main()
main()

