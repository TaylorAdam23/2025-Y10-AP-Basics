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
    # calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)
    #display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")
    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator of evil and greed. ")
