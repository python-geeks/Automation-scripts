import os
import shutil
import time

# 1st part asks the user what folder they want to pull files/data from
print('You are about to move files from one directory to another.')
dirA = input('What directory would you like to move? (please enter full path):')

dirA_exist = os.path.exists(dirA)

# checks if the folder exist or not
while os.path.exists(dirA) is not True:
    dirA = input(f'{dirA} directory does not exist, please try again (please enter full path):')
else:
    # 2nd part is to ask the user where they want to move the contents of a folder to
    dirB = input(f'Where would you like to transfer the contents of {dirA}? (please enter full path):')

    # check's if the destination folder exist or not
    while os.path.exists(dirB) is not True:
        # asks the user if they would like to create the directory
        Q1 = input(f'{dirB} does not exist, would you like to create it (Y/N)?')

        # if they say yes, it is create
        if Q1 == 'Y':
            print(f'Creating {dirB}')
            os.mkdir(dirB)
            print(f'{dirB} created')

        # if they say no, they are asked again where to transfer the files
        elif Q1 == 'N':
            dirB = input(f'Where would you like to transfer the contents of {dirA}? (please enter full path):')

        # if Y or N is not entered, user is asked to try again
        else:
            print('That is not a valid entry, please try again')

    # sets up a endless while loop to continuously move files from one to the other until the code is exited
    running = True
    while running:

        dir_contents = os.scandir(dirA)

        for content in dir_contents:
            content_to_move = dirA + '\\' + content.name
            # skips any folders found
            if os.path.isdir(content_to_move):
                print(f'{content_to_move} is a folder and not a file, skipping')
                continue
            # moves file one at a time
            else:
                shutil.move(dirA + '\\' + content.name, dirB)
                print(f'File {content.name} has been moved')

        # sleeps for 30 seconds till it checks again
        print('sleeping for 30 seconds')
        time.sleep(30)
