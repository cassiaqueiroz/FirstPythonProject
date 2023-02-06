print("Write your age and press Enter: ")
age = int(input())
if age >= 75:
    print("Now Write your name and press Enter: ")
    name = input()
    print("\nWelcome,", name, "! You're ", age, "years old, aren't you?")
    print("Schedule the vaccine electronically or search for unscheduled vaccination locals.")
else:
    print("\nWait for the next phases of the Vaccination Campaign.")

