# Using PdfEncrypt and PdfDecrypt Script

## Steps to encrypt the PDF file :

1. run the script `PdfEncrypt.py` and pass the path of the file as an argument.  
Example :  
    ```
    python PdfEncrypt.py ./test_file.pdf
    ```

2. Enter the password when prompted.  
Example :  
    ```
    password for encrypting : testing_password
    ```
3. You will get the following prompt with the relative path to the encrypted file.
    ```
    FILE HAS BEEN ENCRYPTED SUCCESSFULLY. STORED IN ./test_file.pdf.aes
    ```

## Steps to decrypt the encrypted PDF file : 

1. run the script `PdfDecrypt.py` and pass the path of the file as an argument.  
Example :  
    ```
    python PdfDecrypt.py ./test_file.pdf.aes
    ```

2. Enter the password when prompted.  
Example :  
    ```
    password for encrypting : testing_password
    ```

3. On __Successful decryption__ you will get the following prompt with the relative path to the decrypted file.
    ```
    FILE HAS BEEN DECRYPTED SUCCESSFULLY. STORED IN ./test_file.pdf
    ```
    On __Failure__ you will get the following prompt
    ```
    WRONG PASSWORD OR THE FILE IS CORRUPTED
    ```