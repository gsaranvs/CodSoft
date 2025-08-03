import random
import string

print("Welcome to Password Generator!!!")

lenpas=int(input("Enter The Length of the Password You Want:"))

letters=string.ascii_letters
digits=string.digits
symbols=string.punctuation

char=letters+digits+symbols

pw=""
for i in range(lenpas):
    pw+=random.choice(char)

print("Your Generated Password:",pw)