# print("Hello"[4])
# print("123" + "345")
# 123_456_789 - 123,456,789
#type() what type the code is

## - type conversion
#num_char = len(input("What is your name?"))
#new_num_char = str(num_char)
#print("YOur name has " + new_num_char + " characters")
 
## 🚨 Don't change the code below 👇
#two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
#Check the data type of two_digit_number
# print(type(two_digit_number))
#Get the first and second digits using subscripting then convert string to int.
#first_digit = int(two_digit_number[0])
#second_digit = int(two_digit_number[1])
#Add the two digits together
#two_digit_number = first_digit + second_digit
#print(two_digit_number)

# ** - exponent 
## PEMDAS
#()
#**
#*
#/
#+

##BMI Calculator
# 🚨 Don't change the code below 👇
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
#weight_as_int = int(weight)
#height_as_float = float(height)
# Using the exponent operator **
#bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
#bmi = weight_as_int / (height_as_float * height_as_float)
#bmi_as_int = int(bmi)
#print(bmi_as_int)

#print(round(8 / 3, 2 - round to two decimal places))
#print(8//3) - turns float to int
#print(4/2) - still a floating point number

##result = 4/2
#result /= 2 #a/==b also known as a = a/b
#print()

#score = 0
#height = 1.8
#isWinning = True
#user scores a point
# score += 1 #RHS score +1
# print(score)
#print("Your score is " + str(score)) - convert to String
#print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") #more convient way - f-string

##Age Calculator - days which you will live until 90
#1 year  = 365 days
#1 year = 52 weeks
#1 year = 12 months
#live until 90
# 🚨 Don't change the code below 👇
#age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#age_as_int = int(age)

#Days
#inputage_to_days = int(age)*365
#days_as_int = 365*90
#days_left = days_as_int - inputage_to_days

#Months
#inputage_to_months = int(age)*12
#months_as_int = 12*90
#months_left = months_as_int  - inputage_to_months

#Weeks
#inputage_to_weeks = int(age)*52
#weeks_as_int = 52*90
#weeks_left = weeks_as_int  - inputage_to_weeks

#print(f"You have {days_left} days, {months_left} months, and {weeks_left} weeks left")
#Write your code below this line 👇


##solution
# 🚨 Don't change the code below 👇
#age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#age_as_int = int(age)

#years_remaining = 90 - age_as_int
#days_remaining = years_remaining * 365
#weeks_remaining = years_remaining * 52
#months_remaining = years_remaining * 12

#message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left." 
#print(message)

##Overflow - Example of a bathtub -- 
             ##start
#                |
#                |
#                |
#NO      water level greater than 80cm?   Yes
#|                                         |
#|                                         |
#contiue                                 drain water
#an example of a conditional statement known as an if/else statement 
##Using Python code
#if condition:
#  do this #if the condition isn't true skip to next block
#else:
#  do this 

#water_level = 50
#if water_level > 80:
#  print("Drain Water")
#else:
#  print("Continue")

##Theme park 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:#does not include 120, use >= to include 120#== equal to !=not equal to 
  print("You can ride the rollercoaster!")#inside the if statement of the indentation
else:
  print("Sorry, you have to grow taller before you can ride.")#inside else statement

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


#odd or even
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0 :
    print("This is a even number")
else:
    print("This is an odd number")
#% -- divide then the number left out(output) is the remainder
#7 % 2
#2 + 2 + 2 + 1
#output 1

############################################
age = int(input("How old are you? "))

if age<= 18:
    print("you have to pay $7 ")
elif age > 18: 
    print("you have to pay $12")

#if/elif/else
if conditional1:
       do A - if it's not true check for condition 2 and so on
elif condition2:
       do B
else:
       do this  - none of these conditions are true
#Nested if/else 
if condition:
    if another condition:
       do this 
    else:
        do this
else:
    do this



                 Start
                   |
                   | 
            height > 120cm?
              |        |       
   no         |        | yes
        Can't ride    Can ride
                          |
                          |
                         age 
         18 or under  |            |Over 18
                      |            |
                      $7            $12

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
       print("You can ride the rollercoaster")
       age = int(input("What is your age? "))
       if age <= 18:
              print("Please pay $7.")
       else:
              print("Please pay$12.")
else:
       print("Sorry, you have to grow taller before you can ride.")

                         age 
         under 12         |      |           |Over 18
                      |      |12-18      |
                      $5    $7          $12

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
       print("You can ride the rollercoaster")
       age = int(input("What is your age? "))
       if age < 12:
              print("Please pay $5.")
       els age <= 18                 #line 64 to 66 is the 12-18 catches ppl from 12-18
              print("Please pay$12.")
else:
       print("Sorry, you have to grow taller before you can ride.")

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight 
Over 25 but below 30 they are overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

bmi = round(weight / height ** 2)
if bmi < 18.5:  
    print(f"Your bmi is {bmi}, you are underweight.") 
elif bmi< 25:   
    print(f"Your bmi is {bmi}, you have a normal weight.") 
elif bmi < 30:   
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:    
    print("Your bmi is {bmi}, you are obese.")
else:   
    print(f"Your bmi is {bmi}, you are clinically obese.")

if 
elif...
elif...
elif...
else

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Refer to the flow chart here: https://bit.ly/36BjS2D

if year % 4 == 0:#This line checks if the year is divisible by 4. If it is, the year might be a leap year, so the code proceeds to the next check.
  if year % 100 == 0:#This line checks if the year is divisible by 100. If it is, the year might not be a leap year, so the code proceeds to the next check.
    if year % 400 == 0:#This line checks if the year is divisible by 400. If it is, the year is a leap year.
      print("Leap year.")#If the year is divisible by 400, this line prints "Leap year."
    else:
      print("Not leap year.")#If the year is not divisible by 400, this line prints "Not leap year.
  else:
    print("Leap year.")#If the year is not divisible by 100 but is divisible by 4, this line prints "Leap year."
else:
  print("Not leap year.")#If the year is not divisible by 4, this line prints "Not leap year."'
  '#if/elif/else              Multiple if
#if Condition1:          | if condition1:
#    do A                |     do A
#elif condition2:        | if condition2:
#    do B                |     do B
#else:                   | if condition3:
#    do C                |     do C

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#bill = 0

#if height >= 120:
#  print("You can ride the rollercoaster!")
#  age = int(input("What is your age? "))
#  if age < 12:
#    bill = 5
#    print("Child tickets are $5.")
#  elif age <= 18:
#    bill = 7
#    print("Youth tickets are $7.")
#  elif age >= 45 and age <= 55:
#    print("Everything is going to be ok. Have a free ride on us!")
#  else:
#    bill = 12
#    print("Adult tickets are $12.")
#  
#  wants_photo = input("Do you want a photo taken? Y or N. ")
#  if wants_photo == "Y":
#    bill += 3
  
  #print(f"Your final bill is ${bill}")

#else:
  #print("Sorry, you have to grow taller before you can ride.")
  ##034
  #https://khemlall-mangal.medium.com/day3-learn-python-100-days-of-code-with-khemlall-48c2689dd393
  # 🚨 Don't change the code below 👇
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#bill = 0 

#if size == "S":
#    bill +=15
#elif size == "M":
#    bill += 20
#else:
#    bill += 25

#if add_pepperoni =="Y":
#  if size == "S":
#    bill +=2
#  else:
#    bill += 3

#if extra_cheese == "Y":
#   bill += 1

#print(f"Your final bill is: ${bill}.")
'
'# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")'

###start 037
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#write your code here
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":

  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":

    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")