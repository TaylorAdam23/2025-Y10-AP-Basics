#ask user for width and loop until they enter a number that is more than zero

error = "Please enter a number that is more than zero\n"
while True:

    try:
        # Ask the user for number
        width = float(input("Width: "))
        # Check that the number is more than zero
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)