# print("hello world")
# print('Ola mundo')

#   VARIABLES

age = 21
print("You are " + str(age) + " years")
print("You are", age, "years")
print(f"You are {age} years")  # O MAIS RECOMENDADO

# Integer
age, players, quantity = 22, 2, 5
print()
print(f"You are {age} years")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# Float
gpa = 3.2
distance = 2.5
price = 10.99

print()
print(f"Your gpa is {gpa}")
print(f"You ran {distance}Km")
print(f"The price is ${price}")

# String
name = "Raphael"
food = "pizza"
email = "raphael@gmail.com"

print()
print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# Boolean                Sempre sem aspas e a primeira letra em maiusculo : True, False
online = True
for_sale = False
running = True

print()
print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

if running:
    print("The game is running")
else:
    print("The game is over")

# Tips and tricks
x, y, z = 1, 2, 3
print()
print(x)
print(y)
print(z)

x = y = z = 0
print()
print(x)
print(y)
print(z)




