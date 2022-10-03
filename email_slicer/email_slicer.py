email = input('Enter the email address: ')

print(
    f'''
username: {email.split('@')[0]}
domain: {email.split('@')[1]}
    '''
)