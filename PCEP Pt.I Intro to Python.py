Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> my_name = "Frank" #variable w/ saved string value
... my_name = "Cabezon" #updating variable value
... 
... print("Followers:" + "55")  #expressions = add "string" values
... together w/ a + sign
... or
... followers = "55"
... print("Followers:" + followers) #this might cause an issue; if it does
... use f-string
... 
... my_age = 35  #numbers can be stored within variables as well
... or
... number_of_applications = 5 + 1 #can also add numbers
... print(number_of_applications)
... or
... percent = .33 * 100  #can also multiply and divide numbers
... print(percent)
... 
... number_of_steps = 70  #variables with numbers for calculations
... print("You're on step:")
... print(number_of_steps + 1)
... 
... private = 3  #storing calculation results
... public = 3
... total = private + public
... print("Total posts:")
... print(total)
... 
... power_on = True   #boolean True & False to determine if data is available
... or
... correct = True
... print(correct)
... or
... print("Load Data")
... status = False
print(status)

status = True   #negating operator not
print(not status)
or
morning = True   #store negation in another variable
is_evening = not morning
print(is_evening)

entered_pin = 5440   #equality operator ==
saved_pin = 5443
entered_pin == saved_pin   #outcome will be either true or false
or
print(10 == 10)

3 != 6   #inequality operator !=
or
number_one = 1
number_two = 2
print(number_one == number_two)
print(number_one != number_two)
or
Result = 7 != 10
print(Result)
or
weight = 220
my_weight = weight == 220
print(my_weight)
or
answer = 12
correct_answer = answer == 9

#formatted strings print(f " { } ") allows numbers & strings to be
added in a display
print(f"{2} new messages")
or
new_messages = 2
print(f"{new_messages} new messages)
or
new= 5
read = 2
print(f"{ new - read} unread messages")
or
degrees = 70
print(f"Temperature: {degrees} F")
or
new = 5   #reusing an f-string
status = f"{new} new messages"
print(status)

#comparing numbers w/ less than < or greater than >
print(3<9) #less than
or
print (3>9) #greater than

#or equal to operators <= less than or equal to, >= greater than or equal to
print(3099<=3095)
print(3099>=3095)
or
result = 3 <= 6   #storing the result of a comparison
 print(result)
or
min = 75
max = 100
result = min <= max
print(result)
or
battery_level = 15
low = battery_level <= 15
print("Low battery: ")
print(low)

print("online" == "online")   #comparing strings
print("online" != "offline")
or
fruit_1 = "banana"
fruit_2 = "orange"
print(fruit_1 == fruit_2)
print(fruit_1 != fruit_2)
or
same = "day" != "night"
print("same time of day?")
print(same)
or
previous_leader = "Anna"
new_leader = "Jim"
leader_change = previous_leader != new_leader
print("Did the leader change?")
print(leader_change)

#types = strings "string", integers 39, floats 39.36, boolean (true/false)

#you can check a type is unsure of value type
is_ready = True
print(type(is_ready))
or
cats = "pets"
print(type(cats))
or
grade_avg = 69.69
print(type(grade_avg))

#you can also convert a type into another type
age = "35"  #string to integer int()
print(type(age))
converted_age = int(age)
print(type(converted_age))
print(converted_age)
print(converted_age > 18)
or
password = 909 #numbers to string str()
old_password = "939"
print(str(password))
print(type(password))
print(password == old_password)
or
weeks = 9   #float() turn integer into a float
print(float(weeks))
or
member = true    #boolean to int
not_member = false
value = int(member)
non_value = int(not_member)
print(value)
print(non_value)
or
#bool() to convert a variable into boolean
name = "Sam"
last_name = " "
siblings = 0
shoe_size = 12

bool_name = bool(name)
bool_last_name = bool(last_name)
bool_siblings = bool(siblings)
bool_shoe_size = bool(shoe_size)

print(bool_name)
print(bool_last_name)
print(bool_siblings)
print(bool_shoe_size)

#input () to alter code based on user input; all input enters code as a string
print("What's your name?")
  name_in = input("Enter your name: ")
  print(f"Hi, {name_in}!")

#converting input from string type to integer or float
user_in1 = input("Enter a number: ")
user_in2 = input("Enter another number: ")
number1 = int(user_in1)
number2 = int(user_in2)
result = number1 + number 2
print(f"The sum is {result}")

#First input script
name = input("Hello! What is your name?")
print(f"Nice to meet you, {name}!")
age = input("How old are you?")
bot_age = input("How old do you think I am?")
age_difference = int(age) - int(bot_age)
print(f"You're {age_difference} years older than me. I'm only
{bot_age} years old!")
color = input(What's your favorite color?")
print(f"Oh, {color} is a beautiful color!")
              
SyntaxError: multiple statements found while compiling a single statement
