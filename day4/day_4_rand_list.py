# import random

# # random_integer = random.randint(1,10)
# # print(random_integer)

# # random_float = random.random()
# # print(random_float)

# random_coun = random.randint(0,1)

# if random_coun == 0:
#     print("You got heads")
# else:
#     print("You got tails")

#append add something in the end, extend add more things in the list

# states_of_america = ["Delaware", "Pennsylvania","New Jersey"]
# print(states_of_america[0])
# states_of_america[1] = "Pencilvania"
# states_of_america.extend(["Angeles", "Tobisuar"])
# print(states_of_america)
# import random

# #n = random.randrange()

# friends = []
# name_string = input("Give me the name strings separated by a coma please")
# info = name_string.split(",")
# friends.extend(info)
# n = random.randrange(0,len(friends))
# print(f"the bill will be pay by {friends[n]}")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])