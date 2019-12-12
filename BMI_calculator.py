def BMI(weight, height):
    return weight/(height)**2

your_weight = float(input("enter your weight : "))
your_height = float(input("enter your height : "))

result = BMI(your_weight, your_height)
print("Your BMI Index is", result)
