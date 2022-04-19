# a collection of instructions
# a collection of code
def function1():
    print("ahhhh")
    print("ahhhhh 2")
print("this is outside the function")

function1()

# a mapping
# input or an argument
def function2(x):
    return 2*x

a = function2(3)
# return value or output in this case 6

def function3(x, y):
    return x + y


a = function3(72, 87)
print(a)


# BMI calculator
name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"


result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

# Solution to the task:
# The following function converts miles to kilometers.
# km = 1.6 * miles
def convert(miles):
    return 1.6 * miles

print(str(convert(72)) + "KM")

