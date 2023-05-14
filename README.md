# base64-encoder
University project in Data Security. A simple base64 encoder that can encode and decode images.

```python
# Import the class
from base64_encoder import Base64

# Initialize the object
image_object = Base64('file_name')

# Encode the image and print it
encoded_image = object.encode()
print(encoded_image)

# Decode the base64 data
object.decode(encoded_image)
```

## How it works

### Encoding
First the image data is converted into a binary string, divided into 6 bit chunks and stored. Each 6 bit chunk can be mapped to one of 64 possible values which are ASCII characters based on the base64 table. The characters include 26 uppercase letters, 26 lowercase letters, numbers from 0-9 and the '+' and '/' symbols used for padding. <br><br> 

The bit chunks are then converted into ASCII characters based on the mapping from the base64 alphabet table. For example the chunk '101010' can be mapped to the letter 'q' corresponding to the decimal value 42.<br>

![base64 encoding table](https://media.geeksforgeeks.org/wp-content/uploads/20200520142906/1461.png)

The resulting strings are concatinated back together to form the encoded file. The length of the string will be longer than the original binary data because every 6 bit chunk is represented by a 8 bit ASCII character.

### Decoding

Decoding the message is done by reversing the encoding process. The endoded message is read and each ASCII character is converted to it's 6 bit representation based on the mapping from the base64 alphabet table. The resulting 6 bit chunks are combined into a binary string that get converted to a stream of bytes from which an image is generated.

## Contributors
- [Gjon Hajdari](https://github.com/GjonHajdari)
- [Hekuran Kokolli](https://github.com/hekurani)
- [Haki Hoti](https://github.com/HakiHoti)
- [Gyltene Sfishta](https://github.com/gyltenesfishta)