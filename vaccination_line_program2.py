print("Please enter your age: ")
age = int(input())
if age < 75:
    print("\nWait for the next phases of the Vaccination Campaign.")
    print("\nThank you for participating!")
if 75 <= age <= 95:
    print("Now Enter your name: ")
    name = input()
    print("\nWelcome,", name, "! You are ", age, "years old, right?")
    print("=== Choose Vaccination Local ===")
    print("1 - Enter '1' for vaccination at home;")
    print("2 - Enter '2' for vaccination at the mall.")
    vaccination_local = int(input())
    if vaccination_local == 1:
        print("\nVaccination local: \nAt home.")
        print("\nThank you for participating!")
    else:
        print("\nVaccination local: \nAt the mall.")
        print("\nThank you for participating!")
if age > 95:
    print("\nVaccination local: \nAt home.")
    print("\nThank you for participating!")
