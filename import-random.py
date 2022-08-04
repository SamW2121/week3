#comment again
import random

password = ""


while True:
    password_length = int(input('> '))
    if 0 < password_length < 50:
        break

for i in range(password_length):
    random_integer = random.randint(0,126)
    password += chr(random_integer)
    
print(password,"stuff")
