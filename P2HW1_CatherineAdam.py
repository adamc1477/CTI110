# Calculating the subtotalm sales tax and overall total of five purchased items.
# February 27th 2022
# CTI-110 P2HW1 - Total Purchases
# Catherine Adam
#
# Ask user to enter prices of 5 items individually, have them printed and
# displayed on separate lines
# Calculate subtotal by adding together all of the entered items
# Calculate the sales tax of the item prices entered at 7% by multiplying the
# subtotal by .07
# Calculate the overall total by adding the subtotal to the sales tax amount
# Display the results showing a print of the subtotal, sales tax and total prices


item_one = float(input('Enter the price of item #1: '))
item_two = float(input('Enter the price of item #2: '))
item_three = float(input('Enter the price of item #3: '))
item_four = float(input('Enter the price of item #4: '))
item_five = float(input('Enter the price of item #5: '))

print('-------Results-------')

sub_total = (item_one)+(item_two)+(item_three)+(item_four)+(item_five)

print('Subtotal:',f'{sub_total:.2f}')

sales_tax = (sub_total)*.07

print('Sales Tax:',f'{sales_tax:.2f}')

total_prices = (sub_total)+(sales_tax)

print('Total',f'{total_prices:.2f}')

