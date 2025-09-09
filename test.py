#my first python program from intro part
print("Hello world")
#program on python identation which is a space before e.g., print 
if 5 > 2:
    print("Five is greater than two!")
else:
    exit()
#this is next chap on comments in coding here is example 
#print("Hello world!")
print("hello world!")
#multiple comments can be written
#THIS IS 
#A COMMENT 
#WRITTEN ON 
#MULTIPLE LINES
"""
THIS IS A 
COMMENT WRITTEN 
IN MULTIPLE LINES
""" #THIS IS CALLED DOC STRING generally used as comments for a function which was defined by you in a code

def addition(number1,number2) -> int:
    """Make addition of two number using + operator

    Args:
        number1 (int): number 1 which used to add
        number2 (int): number 2 which used to add

    Returns:
        int: return the number after addition of two number 
    """    
    return number1 + number2
addedNumber = addition(1,2)
#NEXT PROGRAMME ON VARIABLE
#A variable is created the moment you first assign a value to it.
X = 5 #X is of type int
Y = "JOHN" #y is of type string
z = 4 #z is of type int
Z = "ajit" #z is now of type string AND Z will not override z
a = str(3) #a will be '3'
b = int(3) #b will be 3 
c = float(3) #c will be 3.0
print(type(a)) #will return <class 'str'>
print(type(b))
print(type(c))
Y = "JOHN"
#Y IS SAME AS Y 
Y = 'JOHN' 
#NEXT CHAP OF VARIABLE NAME 
myvar = "Hitesh"
my_var = "Ajit"
_my_var = "bhoomi"
myVar = "papu"
MYVAR = "HITESH"
myvar2 = "AJIT"
"""
---> A variable name must start with a letter or the underscore character
---> A variable name cannot start with a number
---> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
---> Variable names are case-sensitive (age, Age and AGE are three different variables) Due to this you can write 
myVariableName (Camel case) or MyVariableName (Pascal Case) or my_variable_name (Snake Case) All this are example of 
multi word Variable names
---> A variable name cannot be any of the Python keywords.
"""
#variable name can have a short name like x and y or a descriptive name like (age, carname, total_volume)
#variable name can not be written as 2myvar or my - var or my var 
#--> Python allows you to assign values to multiple variables in one line
x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)
#--> You can assign the same value to multiple variables in one line
a = b = c = "apple"
print(a)
print(b)
print(c)
#--> If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. 
# This is called unpacking.
Fruits = ["orange", "banana", "cherry"]
x, y, z = Fruits
print(x)
print(y)
print(z)
# This can be written as 
print(x, y, z)
# Output will be orange banana cherry in one line so you can assign X = Good and Y = Morning and print Good Morning in one command
# This is called use of print function to output variables
M = "orange banana cherry"
print(M)
print(x, y, z)
# this both will be same
# You can also use + operator to output multiple variables
print("Ajeet J Panchal")
print(x + " " + y + " " + z)
# Spacebar and double quotes between commas and plus operator are neccesary otherrwise the outcome will be orangebananacherry
# For numbers + operator works as a mathematical operator
p = 5 
q = 10 
print(p + q) # in this spacebar does not matter but it would be great if we use it 
"""
when you try to combine a string and a number with the + operator, Python will give you an error:
so instead of writing 
p = 5 
y = banana
print(p + y)
we should write 
print(p, y)
"""
print(p, y)
# All the above variables are known as global variable as we created it outside the function but it can be used inside as well
def myfunc():
    print ("I have " + y)
myfunc()
# We can create a variable inside a function, with the same name as the global variable
def myfunc():
    y = "strawberries"
    print("I have some " + y)
myfunc()
print("I have some " + y)
#As we can se the print function outside myfunc gave output based on y = banana but print function inside myfunc gave outut based on y = strawberries
#Now variable inside myfunc is local but if we have to define variable inside myfunc but as global then
def myfunc():
    global y 
    y = "strawberries"
myfunc()
print("I have some " + y)
# Also, use the global keyword if you want to change a global variable inside a function.
y = "banana"
def myfunc():
    global y 
    y = "strawberries"
myfunc()
print("I have some " + y)
#Output will be I have some strawberries
#   PYTHON DATA TYPE
""""
Python has the following data types built-in by default, in these categories:

Text Type:  	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:  	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:  	NoneType
"""
#BELOW ARE THE EXAMPLES
#first we will write just as variable then with variable type and then give print command for display of x and type of x
x = "Hello world"
x = str("Hello world")
print(x)
print(type(x))

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 20
x = int(20)
print(x)
print(type(x))

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 20.55
x = float(20.55)
print(x)
print(type(x))
#Float can also be scientific numbers with an "e" to indicate the power of 10.
z = -87.7e100
print(z) #output will be -8.77e+101
print(type(z))

#Complex numbers are written with a "j" as the imaginary part:
x = 1+1j
x = complex(1+1j)
print(x)
print(type(x))

#Type Conversion
x = 1    # int
y = 2.8  # float
z = 1    # complex
#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a) #output 1.0
print(b) #output 2
print(c) #output 1+0j
#Note: You cannot convert complex numbers into another number type.

#random module for random number
import random
print(random.randrange(1, 10)) #output will be random number from 1 to 10

x = ["apple", "banana", "cherry"]
x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))
x = ("apple", "banana", "cherry")
x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))
x = range(6) 
print(x) #output will be range(0, 6)
print(type(x))
x = {"name" : "john", "age" : "30"}
x = dict(name="john", age=30)
print(x)
print(type(x))
x = {"apple", "banana", "cherry"}
x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
x = frozenset(("apple", "banana", "cherry"))
print(x) #output will be frozenset({'banana', 'cherry', 'apple'})
print(type(x))
x = True
x = bool(5)
print(x) #output will be True
print(type(x))
x = b"Hello"
x = bytes(5)
print(x) #Output will be b'\x00\x00\x00\x00\x00'
print(type(x))
x = bytearray(5)
print(x) #output will be bytearray(b'\x00\x00\x00\x00\x00')
print(type(x))
x = memoryview(bytes(5))
print(x) #output will be <memory at 0x000001ED42334AC0>
print(type(x)) #output will be <class 'memoryview'>
x = None
print(x) #output will be none

#PYTHON CASTING 
"""There may be times when you want to specify a type on to a variable. 
This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, 
including its primitive types."""
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# CODE ABOUT STRINGS
print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"') #quotes inside a string
a = """Hello,
    My name is Hitesh.
    I am 26 years old.""" #you can use ' (single quote as well)
print(a)
# Strings are Arrays
print(a[3]) #get the character at position 3, e.g 0=H 1=e 2=l 3=l..
print(len(a)) #will return how much characters does a have 
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)
# To check if a certain phrase or character is present in a string, we can use the keyword 'in'.
print("Hitesh" in a) #will return True
if "Hitesh" in a:
    print("yes, 'Hitesh is there'.")
print("Ajit" not in a) #will return True
if "Ajit" not in a:
    print("No, Ajit is not there.")
# Slicing strings
print(a[10:18])
print(a[:17]) #slicing from start
print(a[5:]) #slicing to end
print(a[-5:-2]) #negative indexes to start the slice from the end of the string
print(a.upper()) #Gives the string in upper case
print(a.lower()) #Gives the string in lower case
print(a.strip()) #removes any whitespace from the beginning or the end
print(a.replace("H", "J")) #replaces a string with another string
print(a.split(",")) #Split the string and will return ['Hello', '\n    My name is Hitesh.\n    I am 26 years old.']
#we can combine strings and numbers by using f-strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
txt = f"The price is {price} dollars"
print(txt)
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)
#Escape Character
"""You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."""

#To fix this problem, use the escape character \"
txt1 = "We are the so-called \"Vikings\" from the north."
txt2 = 'We are the so-called "Vikings" from the north.'
print(txt1)
print(txt2) #Both the methods can be used 
#Boolean Values - True of False
#When you compare two values
print(10 > 9)
print(10 == 9)
print(10 < 9)
#When you run a condition in an if statement
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#The bool() function allows you to evaluate any value
print(bool("Hello"))
print(bool(15))
#can be done like this also
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#Some Values are False here are example
"""bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""
#Use of Bool in Class
"""you have an object that is made from a class with a __len__ function that returns 0"""
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #In this case bool fun will return false because the length of the myclass if 0 
class Car:
    def __init__(self, brand, color):
        self.brand = brand 
        self.color = color

    def __len__(self):
        return len(self.brand)  # Example: Return length of the brand name

myobj = Car("Toyota", "Red")
print(len(myobj))  # ✅ Output: 6 (length of "Toyota")
#AND HERE IS ANOTHER EXAMPLE
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __len__(self):
        return 2  # Since we have two attributes: brand and color

myobj = Car("Toyota", "Red")
print(len(myobj))  # ✅ Output: 2
#Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())
#another example
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#Check if an object is an integer or not
x = 200
"""Python also has many built-in functions that return a boolean value,
 like the isinstance() function, which can be used to determine if an object is of a certain data type"""
print(isinstance(x, int)) 

#PYTHON OPERATORS
#Operators are used to perform operations on variables and values.
"""
   PYTHON DIVIDES OPERATORS IN THE FOLLOWING GROUPS
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""
#Mathematical Operators 
"""
Addition	    x + y	
Subtraction	    x - y	
Multiplication	x * y	
Division	    x / y	
Modulus      	x % y	--> Return the remainder when x is divided by y
Exponentiation	x ** y	--> x=2 y=5 print(x ** y) #same as 2*2*2*2*2 return 32 
Floor division	x // y  --> x = 15 y = 2 print (x // y) #the floor division // rounds the result down to the nearest whole num return 7
"""
#Python Assignment Operators
# =
x = 5 # same as x = 5
# +=
x = 5
x += 3 #same as x = x + 5
print(x)
# -=
x = 5
x -= 3 #same as x = x - 3
print(x)
# *=
x = 5
x *= 3 #same as x = x * 3
print(x)
# /=
x = 5
x /= 3 #same as x = x / 3
print(x)
# %=
x = 5 
x %= 3 #same as x = x % 3
print(x)
# //=
x = 5
x //= 3 #same as x = x // 3
print(x)
# **=
x = 5
x **= 3 #same as x = x ** 3
print(x)
#HERE ARE OTHERS 
# &=  Performs bitwise AND and assigns the result (a &= b → a = a & b)
# |=  Performs bitwise OR and assigns the result (a |= b → a = a | b)
# ^=  Performs bitwise XOR and assigns the result (a ^= b → a = a ^ b)
# >>= Performs right shift and assigns the result (a >>= b → a = a >> b)
# <<= Performs left shift and assigns the result (a <<= b → a = a << b)
# :=  Walrus operator: Assigns a value and returns it in a single expression (x := 10)
# ~  Bitwise NOT: Flips all bits (inverts 0s to 1s and 1s to 0s) (~a = -(a+1))

#COMPARISON OPERATORS
# ==  Equal to: Returns True if both values are equal (a == b)
# !=  Not equal to: Returns True if values are not equal (a != b)
# >   Greater than: Returns True if left value is greater (a > b)
# <   Less than: Returns True if left value is smaller (a < b)
# >=  Greater than or equal to: Returns True if left value is greater or equal (a >= b)
# <=  Less than or equal to: Returns True if left value is smaller or equal (a <= b)

#LOGICAL OPERATORS
# and  Logical AND: Returns True if both conditions are True (a and b)
# or   Logical OR: Returns True if at least one condition is True (a or b)
# not  Logical NOT: Reverses the boolean value (not a → True if a is False, False if a is True)

#IDENTITY OPERATOR
# is      Identity operator: Returns True if two variables refer to the same object (a is b)
# is not  Identity operator: Returns True if two variables do not refer to the same object (a is not b)

#MEMBERSHIP OPERATOR
# in      Membership operator: Returns True if a value exists in a sequence (a in b)
# not in  Membership operator: Returns True if a value does not exist in a sequence (a not in b)

#OPERATOR PRECEDENCE (TAKE A VIEW)

#LIST
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)   #List items are ordered(INDEXED start from 0), changeable, and allow duplicate values
print(len(thislist)) #List Length to determine how many elements in the list
list1 = ["apple", "banana", "cherry"] #string type
list2 = [1, 5, 7, 9, 3] #integer type
list3 = [True, False, False] #Boolean type 
list4 = ["abc", 34, True, 40, "male"] #Mixed data types 
thislist1 = list(("apple", "banana", "cherry", "pineapple")) # note the double round-brackets
print(thislist1)
print(thislist1[1]) # {thislist1[1] = thislist1[-3]}
print(thislist1[2]) #Will give Cherry 0 apple 1 banana 2 cherry 3 pineapple { thislist1[2] = thislist1[-2]}
print(thislist1[-4]) # thislist1[-4] = thislist1[0]
print(thislist1[1:3]) #range will give you 1st and 2nd element
print(thislist1[:2]) #from the start 
print(thislist1[2:]) #upto the end 
print(thislist1[-4:-2]) #will give you -3rd and -4th element but not the -2nd 
if "apple" in thislist1:  #To check something is in there
    print("yes")
if "mango" not in thislist1:   #To check somethis is not in there 
   print("Mango is not there")
thislist1[2] = "Mango"  #Will change cherry and put mango in it 
print(thislist1)
thislist1[1:3] = ["Mango", "watermelon"] #will change 1st and 2nd element as mango and watermelon
print(thislist1)
thislist1 = list(("apple", "banana", "cherry", "pineapple"))
thislist1[1:3] = ["Mango", "watermelon", "Guava"] #now it will delete 1st and 2nd element and put this new three in it 
print(thislist1)
thislist1[1:3] = ["grapes"] #Now it will delete 1st and 2nd element and put Grapes on it
print(thislist1)
thislist1.insert(2, "watermelon") #this will insert watermelon at second position and the remaining items will move accordingly
print(thislist1)
thislist1.append("orange") #this will add orange at the end
print(thislist1)
thislist1.extend(thislist) #this wiill include elements of thislist in thislist1
print(thislist1)
thistuple = ("kiwi", "Ganna")
thislist1.extend(thistuple) #this wiill include elements of thistuple in thislist1
print(thislist1)
thislist1.remove("cherry") #Remove the first occurrence of "cherry"
print(thislist1)
thislist1.pop(6) #will remove 6th element that is apple 
print(thislist1)
thislist1.pop() #will remove Ganna the last element
print(thislist1)
del thislist1[7] #will remove 7th element that is apple 
print(thislist1)
#del thislist1 #THIS WILL DELETE THE LIST 
#thislist1.clear() #THIS WILL CLEAR THE LIST OUTPUT WILL BE []

#Loop Through a List by using for loop 
thislist1 = ['apple', 'grapes', 'watermelon', 'Guava', 'pineapple', 'orange', 'banana', 'cherry', 'kiwi']
for x in thislist1:
  print(x)
for i in range(len(thislist1)):  #By refering to their index
  print(thislist1[i])
i = 0 #DOING ALL THIS WITH WHILE  LOOP 
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#Looping Using List Comprehension which offers shortest syntax for looping through list
[print(x) for x in thislist1]
#List Comprehension 
#Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Here is old way
newlist = []
for x in thislist1:
  if "a" in x:   #this will create a list which has fruits with 'a' in their name 
    newlist.append(x)

print(newlist) #['apple', 'grapes', 'watermelon', 'Guava', 'pineapple', 'orange', 'banana'] here are they
#Here is better way
newlist = [x for x in thislist1 if "e" in x] #this will create a list which has fruits with 'e' in their name
print(newlist) #['apple', 'grapes', 'watermelon', 'pineapple', 'orange', 'cherry']
#THE SYNTAX FOR ABOVE IS 
#newlist = [expression for item in iterable if condition == True] 
#discussed below 
newlist = [x  for x  in thislist1  if  x != "apple"]
#The condition if x != "apple"  will return True for all elements other than "apple",
# making the new list contain all fruits except "apple".
print(newlist) #this will give a newlist where fruits are there other then apple 
#With no if statement
newlist = [x for x in thislist1]
print(newlist) #Now this will give all the fruits in thislist1 as there is no if statement
#in the newlist = [x for x in thislist1] thislist1 is iterable 
# The iterable can be any iterable object, like a list, tuple, set etc.
newlist1 = [x for x in range(10)] 
print(newlist1) #this will give output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#now we add condition
newlist1 = [x for x in range(10) if x < 5]
print(newlist1) #output will be [0, 1, 2, 3, 4]
#in the newlist = [x for x in thislist1] the first x is expression
#The expression is the current item in the iteration, but it is also the outcome,
# which you can manipulate before it ends up like a list item in the new list:
newlist2 = [x.upper() for x in thislist1]
print(newlist2) #this will give all the fruits but in upper case
newhellolist = ['hello' for x in thislist1]
print(newhellolist) #every fruit name will be changed in  hello 
newlist3 = [x if x != "banana" else "chikoo" for x in thislist1]
print(newlist3) #will return a list with chikoo instead of banana
#Sort the list alphabetically and if there are numbers then numerically
#if case sensitive, then results in all capital letters being sorted before lower case letters
thislist1.sort() #like in this case Guava will be first
print(thislist1)
thislist1.sort(key = str.lower) #this command will sort lower case letters first
print(thislist1)
thislist1.sort(reverse = True) #this will sort in reverse alphabetical order
print(thislist1)
thislist1.reverse() #this will reverse the order first will be last
print(thislist1)
#Use the copy() method
mylist = thislist1.copy()
#or we can write
mylist = list(thislist1)
print(mylist)
#or Use the slice Operator
mylist = thislist1[:]
print(mylist)
#JOIN two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#or 
for x in list2:
  list1.append(x)
print(list3)
#or 
list1.extend(list2)
print(list3)


#code for a function
def my_function1():  #this is called defining a function
   print("Hello from my function")    
my_function1()       #this is called calling a function

def my_function2(fname):  #here fname is an argument which we can add in calling 
   print(fname + " Hitesh Panchal")
my_function2("My name is") #here is one argument
my_function2("I am")
my_function2("Myself")

def my_function3(fname, lname):  #here fname and lname both are arguments and function expects two arguments 
   print(fname + " " + lname)
   print("My name is " + fname + " " + lname)
my_function3("Hitesh", "Panchal") #here we provided both the arguments 

def my_function4(*like): #here we put * because we do not know next variables 
   print ("I like " + like[2]) #here we put 2 from tupples 
my_function4("Reading", "Riding a bike", "Travelling") #it will choose 3rd one
 
def my_function5(book2, book1, book3):    #this is keyword argument
   print ("I Like the book " + book3)
my_function5(book1= "Meluha", book2= "Nagvansh", book3= "Gunaho ka Devta" )

def my_function6(**city):   #this is arbitrary keyword argument
   print("I live in " + city["live"] + " and i work in " + city["work"])
my_function6(live = "Ahmedabad", work = "Gandhinagar")

def my_function7(country = "India"): #this is called default parameter value 
   print("I am from " + country)
my_function7("Sweden")
my_function7("America")
my_function7()
my_function7("South Africa")

def my_function8(food): #passing a list as an argument
   for x in food:
      print(x)
fruits = ["Apple", "Banana", "Cherry"]
my_function8(fruits)

def my_function9(x):
   return x * 10
print(my_function9(2))
print(my_function9(3))
print(my_function9(4))

def my_function10(): #function def can not be empty but still need function so pass statement
   pass

def my_function11(x, /):  #if you write my_function(x)
   print(x)               #this whole code is for // positional arguments //
my_function11(3)          #then here my_function(x = 3) // output will be same

def my_function12(*, x):  #Without the *, you are allowed to use positional arguments 
   print(x)               #even if the function expects // keyword arguments //
my_function12(x = 4)

def my_function13(name, message):
   print("Hello " + name + message) #this is a typical code of positional argument
my_function13("Hitesh", " Welcome") #if we change both by each other function will give incorrect ans

#code to combine both the arguments
#Any argument before the / , are {positional-only}, and any argument after the *, are {keyword-only}.
def my_function14(name, live, /, *, age):
   print("My name is " + name + "I am " + str(age) + " I live in " + live)
my_function14("Hitesh", "Bopal", age = 26)
"""// 
  ANOTHER EXAMPLE OF COMBINING BOTH THE ARGUMENTS
  def my_function(a, b, /, *, c, d):
      print(a + b + c + d) here we can write a,b,c,d in any order

  my_function(5, 6, c = 7, d = 8)//
"""
