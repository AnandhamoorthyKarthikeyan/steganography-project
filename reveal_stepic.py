import stepic
from PIL import Image

img = Image.open("encoded.png")

message = stepic.decode(img)

print("Hidden message:", message)
