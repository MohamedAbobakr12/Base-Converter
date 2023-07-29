"""
This program converts a number to different bases.

The user can choose to convert the number to binary, octal, or hexadecimal.

If the user enters an invalid base, the program will print an error message.
"""

def get_bin(number):
    """
    Converts a number to binary.

    Args:
        number: The number to convert.

    Returns:
        The number in binary form.
    """

    x = bin(number)
    x = x[2:]
    return x

def get_oct(number):
    """
    Converts a number to octal.

    Args:
        number: The number to convert.

    Returns:
        The number in octal form.
    """

    x = oct(number)
    x = x[2:]
    return x

def get_hex(number):
    """
    Converts a number to hexadecimal.

    Args:
        number: The number to convert.

    Returns:
        The number in hexadecimal form.
    """

    x = hex(number)
    x = x[2:]
    return x

def get_dec(number):
    """
    Converts a number to decimal.

    Args:
        number: The number to convert.

    Returns:
        The number in decimal form.
    """

    x = number
    return x

x = 1
while (x > 0):
    x = int(input("Enter [1] to Continue \nEnter [0] to Stop\n"))
    if (x == 1):
        try:
            base = int(input("What do you want to convert: "))
            if (base == 2):
                number = int(input("Enter number: "))
                print(get_bin(number))
            elif (base == 8):
                number = int(input("Enter number: "))
                print(get_oct(number))
            elif (base == 16):
                number = int(input("Enter number: "))
                print(get_hex(number))
            else:
                number = int(input("Enter number: "))
                print(get_dec(number))
        except ValueError:
            print("Invalid Input")
    else:
        break