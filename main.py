from base64_encoder import Base64

image_object = Base64('image.png', 'image')
encoded_image = image_object.encode()
# print(encoded_image)

image_object.decode(encoded_image)