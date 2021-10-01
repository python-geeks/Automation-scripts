# Certificate Generator

## Table of Contents

- [Folder Structure](#folder-structure)
- [Requirements](#requirements)
- [Approach](#approach)

## Folder Structure

```plain
│   README.md
│   requirements.txt
│   run.py                                             # To run the web app
│
└───app
    │   routes.py                                      # Contains routes
    │   utils.py                                       # Contains generate_certifcate() function
    │   __init__.py
    │
    ├───static                                         # Contains necessary static files
    │   └───certificates
    │       ├───generated                              # Stores generated certificates
    │       │       Shreyas Vedpathak.png              # sample certificate
    │       │
    │       └───template                               # Contains neccesary required files
    │               Sanchez-Regular.ttf                # Font
    │               template.png                       # Template for certificate
    │
    └───templates                                      # HTML files for frontend
            certificate.html
            download.html
            home.html
```

## Requirements

- Flask==1.1.2
- Pillow==8.3.1

## Approach

1. We get the user name and pr number from the form in `certificate.html`.
2. We use the received information to generate and save the certificate using `generate_certificate()` function in `app/utils.py`.
3. Finally, we render that certificate using `download.html` and we provide the option of downloading, and generate again.
