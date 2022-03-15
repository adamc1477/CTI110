color_1 = int(input())
color_2 = int(input())
color_3 = int(input())

color_list = (color_1, color_2, color_3)

gray = min(color_list)

color_1 = (color_1 - gray)

color_2  = (color_2 - gray)
    
color_3 = (color_3 - gray)

print(color_1, color_2, color_3)