#code1
#print even numbers from 1 to 20 
for i in range(1, 21):   #  loop from 1 to 20
    if i % 2 == 0:       # to check if number is divisible by 2
        print(i)


#code2
#for factorial of a number
num = 10
factorial = 1

for i in range(1, num + 1):   # loop from 1 to num
    factorial = factorial * i     # multiply each i with factorial
print("Factorial of", num, "is", factorial)


#code3
word = "madam" 
if word == word[::-1]: # compare word with its reverse through slicing trick 
    print(word, "is a palindrome")
else: 
    print(word, "is not a palindrome")
word = "Hitesh" 
if word == word[::-1]: # compare word with its reverse through slicing trick 
    print(word, "is a palindrome")
else: 
    print(word, "is not a palindrome")


#code4
#to find largest number
Numbers = [67, 78, 94, 99, 103, 108, 53]
Largest_Number = Numbers[0]     #this will assume that first number is largest
for num in Numbers:
    if num > Largest_Number:
        print("Largest Number is ", Largest_Number)


#Sum of Digits of a Number
num = 8659
total = 0
while num > 0:
    digit = num % 10     # this will get last digit
    total = total + digit       # add digit to total
    num = num // 10      # remove last digit
print("Sum of digits is equal to :", total)



#code6 
#base on 5 sum of two matrices 
#2D array code
a = [[1,2,3], 
     [4,5,6],
     [7,8,9]]
b = [[9,8,7],
     [6,5,4],
     [3,2,1]]
c = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(a)):
  for j in range(len(a[i])):
    print(i,j)
    c[i][j] = a[i][j] + b[i][j]
print(c)   #this will print sum of a and b 


#code7
#code to find fibonacci sequencd
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(20):    # print first 10 terms
    print(a, end=" ")  #end=" " is to add spaces between two numbers 
    a, b = b, a + b
print()


#code8
#to check number  prime or not
num = 29
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):   # check from 2 to num-1
        if num % i == 0:      #will check if number is divisible by any number between 2 and number itself
            is_prime = False
            break
if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

num = 39
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):   # check from 2 to num-1
        if num % i == 0:      #will check if number is divisible by any number between 2 and number itself
            is_prime = False
            break
if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
