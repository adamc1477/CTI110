user_text = input()

count = 0

for i in user_text:
    if not(i in " ,.!"):
        count += 1

print(count)