
if True:   #if statement conditional; runs code only if true
  print("Hello")
or
if False:    #false skips code block
  print("Hello")
#code block beneath a conditional statement uses 2 spaces of indentation
#code block can have infinite lines as long as we follow indentation
or
greeting = True
if greeting:
  print("Hello!")

#conditions to conditional statements
answer = "Tesla"
if answer == "Tesla":
  print(answer + "is correct!")
or
answer = "Edison"
if answer != "Tesla":
  print(answer + "is wrong!")
or
age = 35
if age <= 67:
  print("You still can't retire!")
or
day_time = true
if day_time == true:
  print("Lights off!")
or
score = 51 #storing a comparison in a variable
pass_grade = score > 50
if pass_grade:
    print("Passed!")
or
song = "Don't stop me now"
replay_times = 345
if replay_times >= 300:
    print("Your top song on the week: ")
    print(song)
or
inbox_full = True
show_alert = inbox_full == True
if show_alert:
    print("Inbox full")
or
available = True   #using negation operator
if available:
    print("In Stock")
if not avaible:
    print("Out of stock")
    
available = False   #Else statements; dont need their own condition as it handles cases where if code block doesn't run 
if available:
    print("Out of stock")
else:
    print("In stock")
or
is_daytime = False
if is_day:
    print("Lights off")
else:
    print("Lights on")
or
points = 7600
points_needed = 9000
if points >= points_needed:
    print("You're at level 2")
else:
    left = points_needed - points
    print("Points needed for level 2")
    print(left)

hour = 18   #elif, else/if conditional statements
if hour < 12:
    print("Goodmorning")
elif hour < 17:
    print("Good afternoon")
elif hour < 22:
    print("Good evening")
else:
    print("Goodnight")
or
topping = "pineapple"
if topping == "pineapple":
    print("Great choice")
elif topping == "pepperoni":
    print("Also a good choice!")
else:
    print("Piss or get off the pot!")

age = 17   #and operator; runs code block when all conditions are met. links multiple conditions
has_permit = True
if age > 16 and has_permit:
    print("Can drive")
or
age = 17
has_permit = True
is_insured = True
if age > 16 and has_permit and is_insured:
    print("Can drive")
or
year = 1998
if year > 1890 and year < 2026:
    print("You're living in the times man..")

average_grade = "B" #or operator, runs when one of the conditions are met, links multiple conditions. Only skips if all conditions are false
final_score = 75
if average_grade == "B" or final_score >= 75:
    print("Certificate achieved!")
or
average_grade == "B"
final_score = 1400
won_competition = True
if average_grade == "A" or final_score = 1500 or won_competition:
    print("Certificate achieved!")
or
mobile_wifi = False
cellular = False
if mobile_wifi or wifi:
    print("Loading inbox...")

#Rock, paper, scissors. Find a way to create this code

wallet = 3   #assignment operator, how variables keep track of +,-,*,/ etc. This is called self-assignment, helps track data that changes over time
wallet = wallet
print("wallet")
or
wallet = 3
wallet = wallet + 1
print("wallet")
or
name = ("Account name: ")
name = name + " Elton"
name = name + " John"
print(name)
or
dollars = 0
dollars = dollars + 6
dollars = dollars - 3
print(dollars)

sales = 5   #instead of using variables name constantly can be replaced with += operator
sales = sales + 1 #instead use += to self assign add
sales += 1
print(sales)
or
sales = 5
sales -= 3   #operator to self assign subtract -=
print(sales)


while True:   #while loops are used to repeat lines of code
  print("and again")

#while breaks. to stop a while loop from an infinite loop we use while breaks by creating a variable outside of the loop
keep_going = True
while keep_going == True:
  print("and again")
  keep_going = False

#counter variables are conditions within while loops. to control times a while loop runs start with a variable set to a number
#then use a comparison to compare the variable with a number to
counter = 0
while counter < 4:
  print(counter) #order of code block matters how it counts and prints code block
  counter += 1
or
counter = 0
while counter < 4:
  counter +=1
  print(counter)
or
list_number = 1
while list_number <11:
  print("Add Entry")
  list_number += 1
or
first_counter = 0
while first_counter < 5:
  print("**********---------")
  first_counter += 1
second_counter
while second_counter = 0
while second_counter <4:
  print("-------------------")
  second_counter += 1

#for loops. are used to write code with much less lines of code and easier to understand.
for i in range (4):
  print("*********----------")
for i in range (4):
  print("-------------------")
or
for i in range() # this is the formula to using a  for loop
or
for i in range(6):
  print(i)
  print("For loops are amaaaazzziinnngggg")
or
for x in range(5):
  print("Round:")
  print(x)
or
for i in range(3):
  print("Adding entries...")
print("All entries added")


#Loops practice
i = 1
while i < 5:
  print(i)
  i += 1
or
counter = 1
while counter < 2:
  counter += 1
print(counter)
or
print("*")
line = ""
for i in range(4):
  line += "/"
  print(line)
or
print("Zero to four:")
for repetition in range(5):
  print(repetition)
or

#advanced loop control; continue, break, & else

#continue is used to skip current block & move to next iteration
for i in range(1,6):
  if i == 2:
    continue
  print(i)
or
shopping_list = ["apples", "bananas", "bread", "milk", "chips", "eggs"]
for item in shpping_list:
  if item == "chips":
    continue
  print(f"Don't forget to buy: {item}")
  
#break statement exits loop entirely, no iterations executed when invoked
for i in range(1,6):
  if i == 3:
    break
  print(i)
or
password = "open_sesame"
while True:
  if input("Enter the password: ") == password:
    print("Access granted!")
    break
  print("Incorrect password. Try again.")
  
#Else is executed when loop has finished, wont run if loop is terminated by a break statement
for i in range(1,6):
  print(i)
else:
  print('Loop has ended')
or
for i in range(1,11):
  if i == 5:
    break
  print(i)
else:
  print('Loop has ended')
or
shows = ["The Office", "Parks & Rec", "Mr.Robot"]
for show in shows:
  print(show)
else:
  print("Those are my favorite shows!")
or
tasks = ["pending", "completed", "pending", "pending"]
index = 0
while index < len(tasks):
  if tasks[index] == "completed":
    print(f"Skipping task {index + 1}")
    index += 1
    continue
  print(f"Processing task {index + 1}")
  index += 1

  
