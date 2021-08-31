# Image Steganography 

### Library : 

Numpy , pycrypto 

### Encryption:

Input : Image , message , key
Output : The encrypted image 

The message is encrypted using AES algorithm . The cypher text is then encrypted into the edge of the image.Sobel filter and gaussian filter is used to detect the edges of the image.The code is present in image_steganography.py . 

### Decryption 

Input : Original image , output image , key 

Output: The decrypted text ( Plain text)

The length of the message is identified from the first set of edge pixels. Using the length of the message , the encrypted text is identified and converted to byte format. The cipher text is passes through the AES algorithm which decryots the message using the key.The code is present in Image_steganography_decode.py .

