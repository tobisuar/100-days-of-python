# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)

# student_heights = input("input a list of students heights: ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# total = 0
# for height in student_heights:
#     total += height
# print (total)
# cantindad = len(student_heights)
# promedio = total/cantindad
# print(f"el promedio de altura es {promedio}")    

# student_scores = input("Ingrese las notas de los estudiantes: ").split()

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# max = -1

# for h in student_scores:
#     if h > max:
#         max = h
# print(f"la nota mas alta fue {max}")

# for number in range (1, 11 , 3):
#     print(number)

# total = 0
# for number in range(1,101,2):
#     total+=number
# print(total)

# total2 = 0
# for number in range(1,101):
#     if number % 2 == 0:
#         total2+=number
# print(total2)

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 != 0:
#         print("Fizz")
#     elif number % 5 == 0 and number % 3 != 0:
#         print("Buzz")
#     elif number % 5 == 0 and number % 3 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for nr_letters in range (0,nr_letters):
    x = letters[random.randint(1,len(letters)-1)]
    password = password + x
for nr_symbols in range(0,nr_symbols):
    x = symbols[random.randint(0,len(symbols)-1)]
    password = password + x
for nr_numbers in range(0,nr_numbers):
    x = numbers[random.randint(0,len(numbers)-1)]
    password += x
    
pass_list = password.split()
password = random.shuffle(pass_list)
password = pass_list[0]
print(password)