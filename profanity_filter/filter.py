from better_profanity import profanity
import argparse


# the main function
def main(args: argparse.Namespace) -> None:
    # this will store the passed content
    content = ''

    # if text is passed then read that
    if args.text is not None:
        content = args.text
    else:  # if file is passed then read that file content
        try:  # try to open the file
            with open(args.file) as f:
                for data in f.readlines():
                    content += data
        except FileNotFoundError:  # if file not found
            # \033[91m specifies the red color
            print('\033[91mERROR: file not found\033[0m')
            exit(0)  # exit the program

    # censor the content
    censored = profanity.censor(content)

    # writing censored data to a file if asked
    if args.output is not None:
        with open(args.output, 'w') as f:
            f.write(censored)

            # informing the user
            print(f'\033[92m[+] Censored data written to {args.output}\033[0m')

    # printing the content to the console
    print()
    print('\033[1mCENSORED DATA\033[0m')
    print()
    print(censored)

    # if -f is passed then write the censored data back to the original file


if __name__ == '__main__':
    # argparse obj
    parser = argparse.ArgumentParser()

    # adding a group
    input_grp = parser.add_mutually_exclusive_group(required=True)

    # adding arguments to the group
    # argument for text
    input_grp.add_argument(
        '-t', '--text',
        type=str,
        metavar='',
        help='Specify the string to censor'
    )

    # argument for file
    input_grp.add_argument(
        '-f', '--file',
        type=str,
        metavar='',
        help='Specify the file to censor'
    )

    # argument for output file
    parser.add_argument(
        '-o',
        '--output',
        metavar='',
        help='Specify an output file'
    )

    # parsing the args
    args = parser.parse_args()

    # passing the args to the main
    main(args)
