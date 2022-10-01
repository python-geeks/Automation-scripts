import argparse  # to work with the arguments
import string
import random


# function to generate the password
def get_password(length: int) -> str:
    # creating data
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    numbers = [str(a) for a in range(10)]
    lowercase_characters = string.ascii_lowercase
    uppercase_characters = string.ascii_uppercase

    # variable to hold the password
    password = ''

    # adding one symbol
    password += random.choice(symbols)

    # adding one number
    password += random.choice(numbers)

    # adding one lowercase character
    password += random.choice(lowercase_characters)

    # adding one uppercase character
    password += random.choice(uppercase_characters)

    # now run a for loop starting from the current length of the password
    # all the way to the maxium length to fill in the remaining data
    while len(password) < length:
        # adding all the data together into a one list
        characters = list(lowercase_characters) + list(uppercase_characters)
        data = symbols + numbers + characters

        # getting a random character from the list
        random_char = random.choice(data)

        # if asked to exclude duplicates
        if args.excludeduplicates:
            # if character not already inside the password
            # then add it into the password
            if random_char not in password:
                password += random_char
        else:  # if not asked to exclude duplicates
            # then just add the character without checking
            password += random_char

    # shuffling the generated password to mix every character
    # creating a list of the password
    password_list = list(password)
    random.shuffle(password_list)  # shuffling the list

    # returning the password
    return ''.join(password_list)


# main method
def main(args: argparse.Namespace) -> None:
    # storing the length in a variable
    length = args.length

    # if the value is out of range then inform the user and exit
    if length < 6 or length > 20:
        print('ERROR: -l/--length should be in the range of 6 - 20')
        exit(0)

    # this will hold the final password
    password = get_password(length)

    # printing the password to the user
    print(f'PASSWORD: {password}')


if __name__ == '__main__':
    # creating the argparse object
    parser = argparse.ArgumentParser()

    # adding the length argument
    parser.add_argument(
        '-l', '--length',
        help='Length of the password. [MIN=6], [MAX=20], [DEFAULT = 6]',
        metavar='',
        default=6,
        type=int
    )

    # adding the exclude duplicates argument
    parser.add_argument(
        '-ed',
        '--excludeduplicates',
        action='store_true',
        help='Exculdes duplicate characters from the password'
    )

    # parsing the argument
    args = parser.parse_args()

    # calling the main method with the args
    main(args)
