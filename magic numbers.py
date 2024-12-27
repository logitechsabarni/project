def sum_digits(num):
    return sum(int(digit) for digit in str(num))

def is_magic_number(num):
    while num >= 10: 
        num = sum_digits(num)
    return num == 1

def main():
    number = int(input("Enter a number to check if it's a magic number: "))

    if is_magic_number(number):
        print(f"{number} is a magic number!")
    else:
        print(f"{number} is not a magic number.")

main()
