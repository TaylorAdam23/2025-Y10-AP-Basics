#Ask of users name
username = input("What is your name ? ")

#ask for uesrs favourite number (integer)
fav_num = int(input("What is your favourite number ? "))

#double, halve and square the user's favourite number
double  = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

#greet user
print(f"\nHi {username}, your favourite number is {fav_num}")

#output results of double, halving and squaring fav num
print(f"double {fav_num} is {double}.")
print(f"halve of {fav_num} is {halve}.")
print(f"{fav_num} Squared is {square}.")
print()
print("Have a nie day.")
