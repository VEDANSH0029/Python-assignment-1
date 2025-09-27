import datetime  

print("Welcome to Daily Calorie Tracker!")
print("This program helps you log meals, check total calories, and save report.\n")
meal_names = []
meal_calories = []


num_meals = int(input("How many meals do you want to enter? "))

for i in range(num_meals):
    name = input("Enter meal name: ")
    calories = float(input("Enter calories for this meal: "))
    meal_names.append(name)
    meal_calories.append(calories)


total_calories = sum(meal_calories)
average_calories = total_calories / num_meals

daily_limit = float(input("\nEnter your daily calorie limit: "))

print("\n--- Daily Report ---")
for i in range(num_meals):
    print(f"{meal_names[i]} : {meal_calories[i]:.2f} calories")

print(f"Total calories = {total_calories:.2f}")
print(f"Average per meal = {average_calories:.2f}")

if total_calories > daily_limit:
    status_message = f"You ate more than your daily limit by {total_calories - daily_limit:.2f} calories!"
else:
    status_message = f"You are within your daily limit. Remaining = {daily_limit - total_calories:.2f} calories."

print(status_message)


save = input("\nDo you want to save this report? (yes/no): ")

if save.lower() == "yes":
    with open("calorie_log.txt", "a") as file:
        file.write("\n===== Calorie Tracker Session =====\n")
        file.write("Date & Time: " + str(datetime.datetime.now()) + "\n")
        for i in range(num_meals):
            file.write(f"{meal_names[i]} : {meal_calories[i]:.2f} calories\n")
        file.write(f"Total calories = {total_calories:.2f}\n")
        file.write(f"Average calories = {average_calories:.2f}\n")
        file.write(status_message + "\n")
    print("Report saved to calorie_log.txt")
else:
    print("Report not saved.")