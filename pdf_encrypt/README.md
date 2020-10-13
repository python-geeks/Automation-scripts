# Using pdf_encryptor.py script

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## Steps to encrypt the PDF file :

1. run the script `pdf_encrypt.py` and pass the path of the file as an argument.  
Example :  
    ```
    python pdf_encryptor.py -e test_file.pdf
    ```

2. Enter the password when prompted.  

3. The decrypted file will be saved as an `.aes` file in the working directory.
    ```
    python pdf_encryptor.py -e test_file.pdf

    Will create:
    test_file.pdf.aes
    ```

## Steps to decrypt the encrypted PDF file : 

1. run the script `pdf_encryptor.py` and pass the path of the file as an argument.  
Example :  
    ```
    python PdfDecrypt.py -d test_file.pdf.aes
    ```

2. Enter the password when prompted.  

3. On __Successful decryption__ you will get the following prompt with the relative path to the decrypted file.
    ```
    On successful decryption the file will be saved in the working directory, without the .aes extension.
    ```
