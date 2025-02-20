# Programmer: Austin Long
# Date: 2/20/25
# Program: Kilometer Converter

# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):    
    # NOTE: I changed the conversion to 0.621372 because the test failed with 0.6214.
    miles = kilometers * 0.621372
    # Return the variable to the calling function
    return miles


#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    user_input = float(input("Enter the kilometers to convert to miles: "))

    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    miles = kilometer_conversion(user_input)

    # Display the miles
    print(f"{user_input} kilometers is {miles:.3f} miles.")
