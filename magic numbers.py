def sum_digits(num):
    """Helper function to sum the digits of a number."""
    return sum(int(digit) for digit in str(num))


def is_magic_number(num):
    """Function to check if a number is a magic number."""
    while num >= 10:  # Keep summing the digits until we get a single digit
        num = sum_digits(num)
    return num == 1


def main():
    # Input from the user
    number = int(input("Enter a number to check if it's a magic number: "))

    if is_magic_number(number):
        print(f"{number} is a magic number!")
    else:
        print(f"{number} is not a magic number.")


# Run the program
main()
