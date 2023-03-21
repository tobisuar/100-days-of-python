# print("Welcome to la montaña rusa")

# height = int(input("ingrese su altura en centimetros: "))
# bill = 0
# if height >= 120:
#    print("podes ingresar")
#    age = int(input("Ingrese edad: "))
#    if age >= 18:
#        bill =12
#        print(f"tenes que pagar {bill} $ ")
#    elif age > 12 and age < 18:
#        bill =10
#        print(f"tenes que pagar {bill} $ ")
#    else:
#        bill =7
#        print(f"tenes que pagar {bill} $ ")
#    wana_photo = input("Do you want a photo?")
#    if wana_photo == "Y":
#        bill += 3
#        print(f"tenes que pagar {bill} $ ")
#    else:
#        print(f"tenes que pagar {bill} $ ")
       
# else:
#      print("no podes ingresar")

#get pair

# number = int(input("Ingrese altura CM"))
# rta = number % 2

# if rta == 1:
#     print("el numero es impar")
# else:
#     print("el numero es par")

#bmi calculator
# weight = float(input(" Enter your weight in KG "))
# height = float(input(" Please enter your height in CM "))

# height_in_m = height / 100  # convert height to meters
# bmi = round(weight / (height_in_m ** 2), 2)

# if bmi <18.5:
#     print(f"Your bmi {bmi}, you are underweight")
# elif bmi > 18.5 and bmi < 25:
#     print(f"Your bmi{bmi}, you are normal weight")
# elif bmi > 25 and bmi <30:
#     print(f"You bmi{bmi}, Time to go to the gym obese")
# else:
#     print(f"GO TO THE GYM {bmi}")

#leap year shit

# year = int(input("Ingrese el año correspondiente: "))
# #fist division

# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("This year is Leap")
#         else:
#             print("This year is not leap")
#     else:
#         print("this year is leap")
# else:
#     print("This year is leap") 

#love letter
print("Welcome to the love Calculator")
name1 = input("What is your namer?")
name2 = input("What is their name?")

combine = name1 + name2

lower_case = combine.lower()

a = lower_case.count("a")
u = lower_case.count("u")
t = lower_case.count("t")
i = lower_case.count("i")
auti = a + u + t + i
s = lower_case.count("s")
tt = lower_case.count("t")
i = lower_case.count("i")
c = lower_case.count("c")

stic = s+tt+i+c

autism = str(auti) + str(stic)

print(autism)