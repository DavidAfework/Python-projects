print("Today's date?")
todays_date = input()
print("Breakfast calories?")
breakfast_calories = int(input())
print("Dinner calories?")
dinner_calories = int(input())
print("Snack calories?")
snack_calories = int(input())

sum = breakfast_calories + dinner_calories + snack_calories

print("Calorie content for " + str(todays_date) + ": " + str(sum))