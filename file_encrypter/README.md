# Using file_encrypter and file_decrypter Script

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## Steps to encrypt the PDF file :

1. run the script `file_encrypter.py` and pass the path of the file as an argument.  
Example :  
    ```
    python file_encrypter.py ./test_file.pdf
    ```

2. Enter the password when prompted.  
  
    ___NOTE : The password should satisfy the following criteria :___
    - at least 8 characters in length
    - at least one lowercase character
    - at least one uppercase character
    - at least one digit (0-9)
    - at least one special character [@_!#$%^&*()<>?/\|}{~:]  

    ___Otherwise the password will be classified as weak and you will be asked to enter a strong password as shown below___  
    
    Example : 
    ```
    password for encrypting : testpass
    WEAK Password
    Please enter a strong password
    password for encrypting : Test@1234
    ```

3. You will get the following prompt with the relative path to the encrypted file.
    ```
    FILE HAS BEEN ENCRYPTED SUCCESSFULLY. STORED IN ./test_file.pdf.aes
    ```

## Steps to decrypt the encrypted PDF file : 

1. run the script `file_decrypter.py` and pass the path of the file as an argument.  
Example :  
    ```
    python file_decrypter.py ./test_file.pdf.aes
    ```

2. Enter the password when prompted.  
Example :  
    ```
    password for encrypting : Test@1234
    ```

3. On __Successful decryption__ you will get the following prompt with the relative path to the decrypted file.
    ```
    FILE HAS BEEN DECRYPTED SUCCESSFULLY. STORED IN ./test_file.pdf
    ```
    On __Failure__ you will get the following prompt
    ```
    WRONG PASSWORD OR THE FILE IS CORRUPTED
    ```
