import re

# RFC 5322 compliant regex
# Source: https://emailregex.com/
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


def validate_email(email_address):
    """
    Validate the provided email address according to RFC 5322 guidelines
    :param email_address: email address to check.
    :return: True if the email address is correct, False otherwise.
    """
    return EMAIL_REGEX.fullmatch(email_address)


if __name__ == '__main__':
    email = input("Enter the email_address address: ")
    result = validate_email(email)
    print(email + " is valid" if result else email + " is not valid")
