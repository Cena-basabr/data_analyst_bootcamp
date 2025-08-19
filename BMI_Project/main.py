user_name = input("Enter your name: ")
user_weight = float(input("Enter your weight in pound: "))
user_height = float(input("Enter your height in inches: "))

BMI = (user_weight * 703)/ (user_height * user_height)

if BMI < 18.5:
    print("Dear",user_name,"Your BMI is", BMI,"and you are underweight.")
elif BMI < 25 and BMI >= 18.5:
    print("Dear",user_name,"Your BMI is", BMI,"and you are slightly overweight.")
elif BMI < 30 and BMI >= 25:
    print("Dear",user_name,"Your BMI is", BMI,"and you are overweight.")
else:
    print("Dear",user_name,"Your BMI is", BMI,"and you are obese.")