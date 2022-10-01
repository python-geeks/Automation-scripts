from plyer import notification
from time import sleep
import argparse


# the main function
def main(args: argparse.Namespace) -> None:
    # creating a title
    title = 'Time for a break!'

    # fetching the message
    message = args.message

    # fetching the delay
    delay = args.delay

    # if delay is less than 60 then set the delay to 60 and inform the user
    if delay < 1:
        delay = 1
        print('Warning: Set delay = 1 minute(s) as passed delay < 1 minute(s)')

    # loop to show the messages as long as the user doesn't explicitly stop the script
    while True:
        # waiting for the delay to finish
        sleep(delay * 60)  # minutes * 60 = seconds

        # displaying a notification after delay
        notification.notify(
            title=title,
            message=message,
        )


if __name__ == '__main__':
    # instantiating argparse
    parser = argparse.ArgumentParser()

    # adding argument for delay seconds
    parser.add_argument(
        '-d', '--delay',
        metavar='',
        help='Specify delay time in minutes. [DEFAULT=20]',
        type=int,
        default=20
    )

    # adding argument for custom message
    parser.add_argument(
        '-m', '--message',
        metavar='',
        help='Specify a message for the notification',
        type=str,
        default='You have been working continuously. Consider taking a break.'
    )

    # parsing the args
    args = parser.parse_args()

    # calling the main method by passing the args
    main(args)
