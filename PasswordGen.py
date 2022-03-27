import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "&~#|-\_^@$¤%!?"
all = lower + upper + number + symbol
lengh = 16

password = "".join(random.sample(all, lengh))

print(password)
with open("fichier.txt", "a") as f:
    f.write("#" + " " + password + "\n")


