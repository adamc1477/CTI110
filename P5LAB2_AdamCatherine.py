def feet_to_steps(user_feet):
    steps_walked = int(user_feet / 2.5)
    return steps_walked

if __name__ == '__main__':
    feet_walked = float(input())
    steps_walked = feet_to_steps(feet_walked)
    print(int(steps_walked))