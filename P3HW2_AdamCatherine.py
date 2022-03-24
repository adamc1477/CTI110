#CTI-110
#P3HW2 - Pizza Order
#Catherine Adam
#3.19.22
#
#Build assignment off of P1HW2 Pizza Order assignment.
#Ask user to enter number of students they would like to order pizza for.
#Ask user for number of people that will be sharing each pizza ( 1.5, 2 or 3)
#If user enters 1.5, the program is to do the math and calculate number of
#Whole pizzas user needs to buy. Do the same for 2 and 3.
#If user enters a value OTHER than 1.5, 2 or 3, display an error and notify
#user that they should have entered 1.5, 2 or 3, tell user to run again
#For the correct number for number of people sharing a pizza, calculate the price
#for number of pizzas needed, assuming one pizza costs $5. Add a 6% tax.
#Print results.

student_number = int(input('How many students do you want to order pizza for? '))

people_per_pizza = float(input('Enter number of people per pizza (1.5, 2 or 3): '))

import math

if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
    pizzas_needed = math.ceil(student_number / people_per_pizza)
    pizza_price = pizzas_needed * 5
    # originally I had a separate line to do the math.ceil, using the original number
    # of pizza needed without math.ceil to calculate the price, and this got me the
    # same $71.55 result as the example, however this calculated the price of NOT
    # whole pizzas. Specifiying to ensure it's okay to have the different result here.
    pizza_price_taxed = pizza_price + (pizza_price * .06)
    print('----Pizza Order--------')
    print('Whole Pizzas Needed:', pizzas_needed)
    print('Price of Pizzas: $', f'{pizza_price_taxed:.2f}')
    print('-----------------------')

else:
    print('INVALID ENTRY!!!!')
    print('Should have entered 1.5, 2 or 3')
    print()
    print('Run program again.')


