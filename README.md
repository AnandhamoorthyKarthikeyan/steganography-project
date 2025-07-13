# 🕵️‍♂️ Steganography Project: Hide and Reveal Secret Messages in Images

## 🎯 Aim
To implement image-based steganography using Python by hiding and retrieving secret messages inside PNG images.

## 🛠️ Tools & Technologies
- **Python 3.13+**
- **stepic** – for steganography encoding/decoding
- **Pillow (PIL)** – for image processing
- PNG image (`cover.png`) as carrier

## ✅ Procedure
1. Prepare a clean `.png` image (`cover.png`)
2. Install dependencies:
pip install stepic pillow
3. Run `hide_stepic.py` to hide the message.
4. Run `reveal_stepic.py` to retrieve the message from `encoded.png`.
## 💻 Code Overview

### 🔐hide_stepic.py
Hides a message:
encoded_img = stepic.encode(img, message.encode())

### 🔍reveal_stepic.py
Reveals the hidden message:
message = stepic.decode(img)

## Output
<img width="982" height="131" alt="Screenshot 2025-07-13 225740" src="https://github.com/user-attachments/assets/d956f459-d558-4178-8dc6-5b03d84594f6" />
encoded.png will look the same as cover.png, but contains hidden data.
Terminal output will print the retrieved message.

## ✅ Result
Successfully implemented a basic image steganography system that can embed and extract messages inside images using Python.

