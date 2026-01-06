print("Welcome to Simple Health Checker!")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
sugar = float(input("Enter your sugar level (mg/dL): "))

if sugar < 140:
    print("Your sugar level is normal. Healthy!")
else:
    print("Your sugar level is high. Check with doctor!")
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You are normal weight.")
elif bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese. Try healthy diet and exercise!")
if age > 50:
    print("Since you're above 50, regular health checkups are recommended.")
