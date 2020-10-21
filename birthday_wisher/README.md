# Bday Wish

## Setup and activate virtual environment
For Unix based systems please execute the following command to create venv and install requirements.
```
$ pip install -r requirements.txt
```

### Objectives
- [x] Telegram - birth_day_wish_telegram.py
    Sends "Happy Birth Message to a Number"

    ##### Requirements
        * Telegram API: Please refer to this [link](https://my.telegram.org/auth)
        * Python
        * A Smart Phone with telegram installed.
    
    ##### Usage:
    `api_id`, `api_hash` and `token` should be applied within `birth_day_wish_telegram.py`
    ```
    api_id = '<API ID>'
    api_hash = '<API HASH>'
    token = '<Bot Token>'
    ```
    [ ] TODO: Improvement needed.
    Desired date can be applide within `birth_day_wish_telegram.py`.
    ```
        while True:
        today = datetime.date.today()
        if today != datetime.date(2020, 10, 15):
            time.sleep(60 * 60 * 24)
        else:
            send_message("Happy Birth Day")
    ```
    
    simply execute the script:
    ```
    python3 birth_day_wish_telegram.py
    ```
    Please take `screen` and/or `tmux` into account.

- [ ] Facebook

- [ ] Twitter

- [ ] Any further idea, Please open an [Issue](https://github.com/python-geeks/Automation-scripts/issues/new/choose)


