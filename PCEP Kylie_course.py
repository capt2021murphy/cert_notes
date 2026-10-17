print('hello')

#Date Types

#comment

#integer
1
1000
38

#float
1.1
3.44
3.1415

#comlpex
1 + 3j

#boolean
0 or 1
True or False 
1>5 #this is the equivalent of false 

#strings - character values, declared using single or double quotes
'whats up'
"whats up"
'1' #not a number but represents character 1 

#collections - a collection of values

#list - collection of values in specific order 
[1,2,3,'a']
#tuple - collection of values in specific order that is immutable
(1,2,3,'a')
#set - collection of values that is unordered and doesnt allow duplicates 
{1,2,3}
{1,2,2,'a'} #is really {1,2,a} since duplicates aren't allowed
#dictionary - collection of unordered key value pairs 
{1:'a'} #this means that everytime you use 1 it maps out to a, like a map legend
{1:'a', 2:'b', 3:'c'}

#Operators

#arithmetic operators

# +, - *, /, ** (power)
1+2 #if you want this to show in terminal must use print function 
print(1+2) #like this 
10-5
(1+3j)**5 #** sign is to the power of, noticed it doesnt work unless writing code in cmd
'a' + 'b' = 'ab' #can be used on strings and lists

#variables
x = 3 #3 is assigned to the letter x

#comparison operators
# <, >, <=, >= #in order less than, greater than, less than or equal, greater than or equal
# != doesn't equal, == equals
1>5
2<=4
'a' == 'd'
'a' != 'd'

#logic operator; and, or, not
1==1 and 1<2 #this would be true
1==2 and 1<2 #this would be false 
1==1 or 1==2 #only 1 has to be true to be true 
False or False 
True or False 
not True #this is false, negation operator

#membership evaluators; checks if something is in a collection (lists, tuples, sets)
1 in [1,2,3] #this would be true
1 not in [1,2,3] #false as 1 is in list

#Variables & mutability v. immutability

#variables - values that are stored in memory that can be changed in the future 
name = 'Frank' 
x= 10
1=x #this is a no-no, variables can't start with a number syntax err
Koolio = 'Gangstas paradise'#case sensitive these are 2 seperate variables
koolio = 'gangstas paradise' #case sensitive these are 2 seperate variables
#variables can only contain alphanumeric & underscores
chain$moker = 'weed' #syntax err because of special characters

#mutability
s = [1, 2, 3] #mutable collection list 
s[1] = 5 #how to change a value inside of list; 0 indexing so 1 = second item in list
t = (1, 2, 3) #tuple collection; immutable
t[1] #this whill show the int 2 in the tuple collection
t[1] = 5 #this will return as an err since tuples are immutable (type error)

#mutability in strings
string = 'string' #defining variable
string = string + 's' #updating variable; strings aren't inherently mutable, you must update variable
string += 's' #shortcut to update variable; += assignment operator
x = 1 
x += 1 #another example of above operator

#mutability in lists & having 2 variable pointed to the same list
>>> my_list = ['q', 'w', 'e'] #2 seperate variables w/ 2 seperate lists
>>> your_list = ['q', 'w', 'e']
>>> my_list
['q', 'w', 'e']
>>> your_list
['q', 'w', 'e']
>>> my_list[0] = 'a'
>>> my_list
['a', 'w', 'e']
>>> your_list
['q', 'w', 'e']
>>> your_list = my_list
>>> your_list
['a', 'w', 'e']

a_list = [1, 2, 3] #2 seperate variables pointed to the same list
b_list = a_list
a_list
[1, 2, 3]
b_list
[1, 2, 3]
a_list[0] = 5
a_list
[5, 2, 3]
b_list
[5, 2, 3]

#Conditionals; if, elif (else/if), else

if #if (condition):then (action), if condition is met:action is executed       
house_music = 10

print('Do you like house music?')

if house_music > 7: #indentation matters as this is associate code block
    print('DUH')
    print('you got great taste in music m8')
    print('you should be a dj')
elif house_music >5:
    print('Not your cup of tea?')
elif house_music >=3:
    print('WHATTT?!?!?')
else:
    print('you need better taste in music m8')


print('<3 house music')

#While & For loops 

#While loop - set of statements as long as condition is true
i = 1
while i < 5:
    print(i)
    i += 1   #short for i = i + 1
print('finished')

#For loop - used to iterate(go over) over a sequence, list, set, string, tuple
name = 'frank' 
for letter in name: #doesn't have to be letter can use x in place, see below
    print(letter)

list = ['guitar', 'code', 'produce', 'piano', 'workout', 'repeat']
for x in list: 
    print(x)
print('Finished')

#loops inside of loops, nested loops
adjs = ['shiny', 'purple', 'short']
nouns = ['roof', 'heart', 'dog']

for adj in adjs:
    for noun in nouns:
        print(adj,noun) 

#control flow; break - exits loop entirely. continue - skips code block

#break
list = ['guitar', 'code', 'produce', 'piano', 'workout', 'repeat']
for x in list: #break in for loop
    print(x)
    if x == 'piano':
        break
print('Finished')

i = 1 #break in while loop
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print('Finished')

#continue
list = ['guitar', 'code', 'produce', 'piano', 'workout', 'repeat']
for x in list: 
    if x == 'piano':
        continue
    print(x)
print('Finished')

#Functions - code block that runs when called with parameters & return values

#Fun-Funk-tions
#creating functions
def penny(): #this defines the function must be in this format
    #code block that's executed when function is called
    print('woofers')
penny() #use this to call function

def penny(age): #inside () are the parameters
    #code block that's executed when function is called
    print(age)
    if age <= 3:
        print('puppers')
    elif age <= 6:
        print('optimus prime')
    else: 
        print('vieja')
    print('woofers')

penny(float(input('Doggos age?: '))) #argument -data used to pass into function when called 
#above is argument with a float input to run function

def penny(age = 15): #auto assigns age parameter to argument if nothing is defined
    #code block that's executed when function is called
    print(age)
    if age <= 3:
        print('puppers')
    elif age <= 6:
        print('optimus prime')
    else: 
        print('vieja')
    print('woofers')

print('Real age')
penny()
print('\nImaginary age')
penny(float(input('Doggos age?: ')))

#print - shows to person running program v return - returns data to orignal place where function was called
def add_1(x):
    return x+1

y = add_1(5)
print(y)

#vs

def add_1(x):
    print(x+1) #this wont return add_1 into function

y = add_1(5)
print(y) #will print none as nothing is returned into function

#or to print and return 
def add_1(x):
    print(x+1) #this wont return add_1 into function
    return x+1
y = add_1(5)
print(y) #will print none as nothing is returned into function



#Compound types; Tuples, Sets, Dictionaries

#Tuples - sequence containing other objects (ints,floats,boolean,none,other tuples); immutable 
x = (7,-7.8,'blue') #example of a tuple 
x[1] = -7.8 #can index like a list
x + (1,2,4) = (7.-7.8,'blue',1,2,4) #concatonation 
x == (7,-7.8,'blue') = True #can compare tuples (boolean)

#Dictionary - mapping between key and value; like a translator or map legend.
eng_to_spa = {} #curly brackets define that it's a dictionary 
eng_to_spa['Hello'] = "Hola" 
print(eng_to_spa)

#or another way to map a dictionary 

eng_to_spa = {'Hello' : 'Hola'}
print(eng_to_spa)

#won't work if you try to look up 'Hola" as that is not a key but the value

#Set - group of non-repeating objects
my_set = {1,2,3} #denoted as curly brackets as well but doesn't have pairs, unlike a dictionary 

#or another way to write a set out 
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(1) #this one won't print, but won't cause error 
my_set.add(3)
print(my_set)

#to check for an element in a set you must use IN keyword since there is no indexing 
answers = {'yes','no'}
for answer in answers:
    print(f'Response: {answer}')

#to remove an element from a set 
classes = {'Music', 'French'}
if 'French' in classes: 
    classes.remove('French')

#turning a list into a set to eliminate duplicates
groceries = ['milk', 'honey', 'bread', 'milk']
print(set(groceries))

