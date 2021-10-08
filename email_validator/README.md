# Email Validator

Feature-rich email verification service helping to reduce email bounce, improve email deliverability and increase marketing ROI.

## Features

There are several advanced metrics to help you make informed decisions. Some of these are listed here:

* **Role email address detection:** Role addresses are not associated with a person. Instead, they represent a group, department or role. Example: ```sales@yahoo.com```
* **Disposable email detection:** Detects temporarily created email addresses. Example: ```example@mailinator.com```
* **Free email validator:** The email address is flagged accordingly if it uses a known free email service like Gmail, AOL, Hotmail etc.
* **Email typo correction:** If the address a user keyed in has typos, the built-in auto correction feature suggests the correct email to end users when a domain is spelled incorrectly.
* **MX Record Detection**
* **MX Domain Detection**
* **Strong encryption for complete security.**

## Modules Used

* quickemailverification
* openpyxl

## Dependencies

Email Validator depends on third party libraries and you will first need to install the application's dependencies:

```bash
  pip install -r requirements.txt
```

## Setup

1. Get the QuickEmailVerification API by registering [here](https://quickemailverification.com/register).
2. [Enable](https://quickemailverification.com/settings/2fa) Two-Factor Authentication.
3. Go to [API Settings](https://quickemailverification.com/apisettings) and set an API name and enter your password. The API Key will now be generated.
4. Paste it in ```config.py```

## Run Locally

Clone the project

```bash
  git clone https://github.com/python-geeks/Automation-scripts.git
```

Go to the project directory

```bash
  cd Automation-scripts/email_validator 
```

Enter the list of emails to verify in email_list.txt such that there is one email in each line.
![input_format](https://user-images.githubusercontent.com/75522742/136576104-242e8912-26c7-4bcf-b8de-8313de57ec3c.png)

Run ```main.py```

```python
  python main.py
```

After a few seconds, ```result.xlsx``` would be created which would contain the full report.
![sample_output](https://user-images.githubusercontent.com/75522742/136576305-aed22381-4f97-43a6-a925-409fda533b3a.png)
