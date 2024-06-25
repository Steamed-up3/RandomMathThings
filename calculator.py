"""
Basic Functions:
 - Add
 - Subtract
 - Divide
 - Multiply
 - BODMAS

Slightly More Advances Features:
 - Sin
 - Cos
 - Tan
 - Sin^-1
 - Cos^-1
 - Tan^-1
 - Standard Form
 - Storing values as variables e.g. x/y
 - x^n
 - root(n, x)
 - Conversions between decimal and fraction and recurring decimal

Can check if float is whole number by checking integer conversion is equal to float conversion.
"""


def main():
    while True:
        try:
            numValues = int(input('Enter How many variables/constants will be used: '))
            break
        except ValueError:
            print('Invalid.\n')

    numbers = []
    for i in range(numValues):
        while True:
            try:
                numbers.append(int(input('\nEnter a number: ')))
                break
            except ValueError:
                print('Invalid.')

    print(numbers)


if __name__ == '__main__':
    main()
