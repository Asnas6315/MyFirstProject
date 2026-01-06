print("Welcome to Simple Health Checker!")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
sugar = float(input("Enter your sugar level (mg/dL): "))
if sugar < 140:
    print("Your sugar level is normal. Healthy!")
else:
    print("Your sugar level is high. Check with doctor!")
if age > 50:
    print("Since you're above 50, regular health checkups are recommended.")
