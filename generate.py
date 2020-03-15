import random

lenght = int(input("Lenght: "))

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-/*!&$#?=@<>1234567890'

password = ''

while len(password) != lenght:
    
    password += random.choice(char)

print(password)