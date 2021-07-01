print("What is your name?")
name = input()

print("How old are you?")
age = int(input())

print("How tall are you?")
height = float(input()) 

print("How much do you weight?")
weight = float(input())

bmi = weight / (height **2)

#print(f"{name} you are {age} years old and your bmi is {bmi}")

#print(name + " you are"+ str(age) + "years old and your bmi is" + str( bmi) )

print("{} you are {} years old and your bmi is {:.2f}".format(name, age, bmi))