import os
import argparse


# function to generate a pattern
def get_pattern(level: int) -> str:
    # getting the number of spaces required
    spaces = 2 * (level + 1)

    # getting the number of separators required
    separators_length = spaces // 2

    # generating the pattern
    pattern = ''

    for i in range(separators_length):
        pattern += '  |'

    # adding the finishing
    pattern += '__'

    return pattern


# function to print the structure
def print_structure(path: str, level: int) -> None:
    # printing the dir name
    if level == 0:  # if it is the root directory then print the name as it is
        print(path)
    else:  # if it is not the root directory
        # if dir name is something like dir/indir/then make it indir/
        if '/' in path:
            # the header information should start with level - 1
            print(f'{get_pattern(level - 1)}{path.split("/")[-1]}/')
        else:
            # if dir name is dir then show the user dir/
            # so that it is clear that it is a directory
            print(f'{get_pattern(level)}{path}/')

    # list the contents of the dir
    contents = os.listdir(path)

    # iterating through the each content
    for content in contents:
        # joining the path and the content name
        full_path = os.path.join(path, content)

        # checking if the content is the file
        if os.path.isfile(full_path):
            # if it is then print the file name
            print(f'{get_pattern(level)}{content}')
        else:  # if it is a dir instead
            # add spacing vertically b/w different folders if requested
            if args.spacing:
                print(get_pattern(level)[:-2])

            # call the print_structure function again with the new path
            print_structure(full_path, level + 1)

    # return if all the content of the folder has been iterated
    return


# the main function
def main(args: argparse.Namespace) -> None:
    # simplifying the arguments
    dir_path = args.directory

    # if the passed directory name is invalid then inform the user and exit
    if not os.path.isdir(dir_path):
        print('ERROR: can not find the path specified!')
        exit(0)

    # printing the structure for the given path and the level
    print_structure(dir_path, 0)


if __name__ == '__main__':
    # creating the argparse object
    parser = argparse.ArgumentParser()

    # creating an argument for the directory
    parser.add_argument(
        '-d', '--directory',
        metavar='',
        help='path to the directory. [DEFAULT=\'.\']',
        type=str, default='./'
    )

    # adding argument for vertical spacing b/w folders
    parser.add_argument(
        '-s', '--spacing',
        action='store_true',
        help='Add spacing b/w folders output vertically'
    )

    # parsing the arguments
    args = parser.parse_args()

    # passing the args to the main method
    main(args)
