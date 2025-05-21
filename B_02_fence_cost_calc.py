# ask user for width and loop
# until they enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # Ask the user for number
            response = float(input(question))

            # Check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
# main Routine starts here

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("Cost per meter: ")
    # calculate area / perimeter
    perimeter = 2 * (width + height)
    cost = (perimeter * cost)
    #display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${cost:.2f} ")
    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator of evil and greed. ")
