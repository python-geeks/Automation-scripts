# Python Email validator

Validates email addresses according to RFC 5322 rules. **Note**: a valid email might not exist. This code just checks if the address adheres to the official guidelines, but doesn't connect to any mail server.

Can be used as a script (`python email_validator.py`) or imported into other projects by using the `validate_email()` function.

Requires Python 3.4+ and no extra modules (just 're').
