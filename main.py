#Password Generator Project
import random
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
try:nr_letters= int(input("How many letters would you like in your password?\n"))
except:
    print("Invalid Value Entered!!")
try: nr_symbols = int(input(f"How many symbols would you like?\n"))
except:
    print("Invalid Value Entered!!")
try : nr_numbers = int(input(f"How many numbers would you like?\n"))
except:
    print("Invalid Value Entered!!")

password = []
for char in range(0,nr_letters):
    password.append(random.choice(letters))

for num in range(0,nr_numbers):
    password.append(random.choice(numbers))

for sym in range(0,nr_symbols):
    password.append(random.choice(symbols))

r.shuffle(password)
final_pass = ""
for val in password:
    final_pass += val
print(f"Generated password is : {final_pass}")
