current_price = int(input())

last_months_price = int(input())

change_price = current_price - last_months_price

est_month_mort = current_price / 235.294

print(f'This house is ${current_price}. The change is ${change_price} since last month.')
print(f'The estimated monthly mortgage is ${est_month_mort:.2f}.')

