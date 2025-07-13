import stepic
from PIL import Image
img = Image.open("cover.png")

message = "This is a secret message!"

encoded_img = stepic.encode(img, message.encode())

encoded_img.save("encoded.png")

print("Message hidden successfully in encoded.png!")
