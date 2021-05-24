import math

#take an input
usr_input = input("Enter Your Height in feet and inch eg. 5.6 \n=> ")

#checks wheather user inputted right formatted height
#but that counts 5.11.5 as error because that cant be a float so checking on the first digit by splitting the input
while True:
  try:
    str(float(usr_input.split('.',1)[0]))
    break
  except ValueError:
    usr_input = input("Please Enter Correct Height (Numbers only): ")

#when there is no floating point in height like 5feet only
try:
  feet , inch = usr_input.split('.',1)
except:
  feet = usr_input
  inch = 0

# change that input to centimetermeter
height_cm = float(feet)*30.48 + float(inch)*2.54

# use bmi formula for 18bmi and 25 bmi bmi = weight/(height)^2 or weight = bmi * (height in meter)^2
weight_min = 18 * (height_cm/100)**2
weight_max = 25 * (height_cm/100)**2

# use the result to create an optimal bmi string eg. 75 - 95
print(f"\nYour optimal weight would be: {weight_min:.2f}kg - {weight_max:.2f}kg")


# 1 inch = 2.54cm
# 1 feet = 30.48cm 