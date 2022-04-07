# CTI-110
# P4HW2 - Pizza Order
# Catherine Adam 
# April 5th, 2022
#
# Have user enter the number of students to order pizza for and the number of
# students per pizza. If incorrect entry, give error and prompt user to re-enter.  
# When correct value is entered, calculate whole pizzas needed and price with
# tax included and display them. Ask the user if they would like to run the
# program again, and end the program if they do not.


import math
def main():
    student_number = int(input('How many students do you want to order pizza for? '))

    while True:
        print('Enter number of people per pizza (1.5, 2 or 3): ',end='')
        people_per_pizza = float(input())

        if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
            pizzas_needed = math.ceil(student_number / people_per_pizza)
            pizza_price = pizzas_needed * 5
            pizza_price_taxed = pizza_price + (pizza_price * .06)
            print('----Pizza Order--------')
            print('Whole Pizzas Needed:', pizzas_needed)
            print('Price of Pizzas: $', f'{pizza_price_taxed:.2f}')
            print('-----------------------')
            print()
            print('Would you like to run program again (y for yes): ',end='')
            run_again = input()

            if run_again != 'y':
                break

            else:
                main()

        else:
            print('-----------------------')
            print('INVALID ENTRY!!!!')
            print('Should have entered 1.5, 2 or 3')
            print('Try Again.')
            print('-----------------------')
main()
    


