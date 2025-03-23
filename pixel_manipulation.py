from PIL import Image
import numpy as np
from art import *
import random

tprint ("PIXEL MANIPULATION")
def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)

    np.random.seed(key)  
    indices = np.random.permutation(pixels.size)  

    flat_pixels = pixels.flatten()
    encrypted_pixels = flat_pixels[indices].reshape(pixels.shape)

    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)

    np.random.seed(key)
    indices = np.random.permutation(pixels.size)

    flat_pixels = pixels.flatten()
    decrypted_pixels = np.zeros_like(flat_pixels)

    decrypted_pixels[indices] = flat_pixels 
    decrypted_pixels = decrypted_pixels.reshape(pixels.shape)

    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")


random_key = random.randint(100000, 999999)
stop = True
while True: 

    input_image = input("Enter the full path of the image :- \n")
    option = input("Type 'e'to encrypt or 'd' to decrypt:- \n")
    if option=="e":
        encrypt_image(input_image, "encrypted.png", random_key)
        print(f"Your key for this image is {random_key}")
    elif option == "d":
        user_key = int(input("Enter decryption key: "))
        if user_key == random_key:
            decrypt_image(input_image, "decrypted.png", user_key)
        else:
            print("wrong key can not decrypt")
    else:
        print("YOU have chosen wrong option")
    restart = input ("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        stop = False
        tprint("GOODBYE")