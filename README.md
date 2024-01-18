# base64-encoder
University project in Data Security. A simple python base64 encoder that can encode and decode messages, images and videos.

## Syntax

The `mode` parameter can be `'string'`, `'image'` or `'video'`. 

```python
# import the class
from base64_encoder import Base64

# initialize the object with the message or file and type parameter
b64 = Base64(message_or_file, mode)

# encode the data and print it
encoded_output = b64.encode()
print(encoded_output)

# decode the base64 data
b64.decode(encoded_output)
```

> **Note:** although video encoding works, decoding is currently not implemented.

## How it works

### Encoding
First the data is converted into a binary string, divided into 6 bit chunks and stored. Each 6 bit chunk can be mapped to one of 64 possible values which are ASCII characters based on the base64 table. The characters include 26 uppercase letters, 26 lowercase letters, numbers from 0-9 and the '+' and '/' symbols used for padding.

The bit chunks are then converted into ASCII characters based on the mapping from the base64 alphabet table. For example the chunk '101010' can be mapped to the letter 'q' corresponding to the decimal value 42.<br>

| ![base64 table](https://media.geeksforgeeks.org/wp-content/uploads/20200520142906/1461.png) |
|:--:|
| *Base 64 alphabet table* |


The resulting strings are concatenated back together to form the encoded file. The length of the string will be longer than the original binary data because every 6 bit chunk is represented by an 8 bit ASCII character.

### Decoding

Decoding the message is done by reversing the encoding process. The encoded message is read and each ASCII character is converted to it's 6 bit representation based on the mapping from the base64 alphabet table. The resulting 6 bit chunks are combined into a binary string that generates our data back.

For messsages the binary string is split into 8 bit chunks, converted to an integer and then an ASCII character from it's integer value. For images the binary string gets converted to a stream of bytes from which an image is generated.

## Contributors
- [Gjon Hajdari](https://github.com/GjonHajdari)
- [Hekuran Kokolli](https://github.com/hekurani)
- [Haki Hoti](https://github.com/HakiHoti)
- [Gyltene Sfishta](https://github.com/gyltenesfishta)
