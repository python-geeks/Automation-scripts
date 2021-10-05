import os
import base64


def encoder():
    img_file = os.listdir('encode_image/')
    print('file to be encode: ', img_file)
    for image in img_file:
        with open("encode_image/" + image, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_message = base64_encoded_data.decode('utf-8')

            print(base64_message)
            f = open('encoded.txt', 'w')
            f.write("data:image/png;base64," + base64_message)
            f.close()


if __name__ == '__main__':
    encoder()
