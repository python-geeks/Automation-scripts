from twilio.rest import Client

sid = 'ACCOUNT SID goes here'
auth_token = 'AUTH token here'

twilio_number = 'Your Twilio provided number here'

client = Client(sid, auth_token)

details = {'Message created': '', 'Date sent': '', 'Body': ''}


def craft(msg, fromPhone, sendTo):
    message = client.messages.create(
        body=msg,
        from_=fromPhone,
        to=sendTo
    )

    details['Message created'] = str(message.date_created)
    details['Date sent'] = str(message.date_sent)
    details['Body'] = str(message.body)


def main(msg: str):
    return craft(msg, twilio_number, '+15555550100')


if __name__ == '__main__':
    main('Hello, user! Sent from Python!')
    seeDetails = input('See details of this message? [y/n]: ')
    if seeDetails.lower() == 'y':
        for i in details:
            print(f'{i} = {details[i]}')
    else:
        exit()
