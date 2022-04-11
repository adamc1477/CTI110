def laps_to_miles(user_laps):
    laps_to_miles = user_laps * miles
    return laps_to_miles

miles = 0.25 

if __name__ == '__main__':
    print(f'{laps_to_miles(user_laps = float(input())):.2f}')