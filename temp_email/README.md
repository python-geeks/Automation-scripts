# This is a script that uses a temporary email service for registering throwaway accounts. 
 
- First, install the requirements by `pip install -r requirements.txt`
- To Run, use the following command
 
    ```python3 temp_email.py```
 
- For usage help, run `python3 temp_email.py -h`

- You can also use the `MailDrop` class in your other projects
 
    ```python3
    from temp_email import MailDrop
    
    md = MailDrop(address="re-used-address", message_filter="Complete your Sign-Up")
    msgs = md.get_emails()
    for msg in msgs:
        print(msg)
    ```

See the docstrings of the class' functions for more info on possible uses.
