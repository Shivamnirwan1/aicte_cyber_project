import cv2
import os
import random
import hashlib
import numpy as np

def generate_positions(password, msg_length, img_shape):
    random.seed(hashlib.sha256(password.encode()).hexdigest())  # Seed RNG with password
    positions = []
    used_positions = set()
    
    while len(positions) < msg_length:
        x = random.randint(0, img_shape[0] - 1)
        y = random.randint(0, img_shape[1] - 1)
        z = random.randint(0, 2)
        if (x, y, z) not in used_positions:
            positions.append((x, y, z))
            used_positions.add((x, y, z))
    
    return positions

def encrypt_image(image_path, msg, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read the image.")
        return None
    
    if len(msg) > img.shape[0] * img.shape[1]:
        print("Error: Image too small for message.")
        return None
    
    d = {chr(i): i for i in range(255)}
    positions = generate_positions(password, len(msg), img.shape)
    
    for i, char in enumerate(msg):
        x, y, z = positions[i]
        img[x, y, z] = np.uint8(d[char])  # Ensure pixel values remain valid
    
    encrypted_image_path = "encryptedImage.png"  # Use PNG to avoid compression
    cv2.imwrite(encrypted_image_path, img)
    print(f"Encrypted image saved as {encrypted_image_path}")
    os.system(f"start {encrypted_image_path}")
    return encrypted_image_path

def decrypt_image(image_path, msg_length, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read the image.")
        return None
    
    c = {i: chr(i) for i in range(255)}
    positions = generate_positions(password, msg_length, img.shape)
    
    message = "".join(c[int(img[x, y, z])] for x, y, z in positions)  # Ensure correct mapping
    return message

def main():
    image_path = "arflow.jpg"  # Replace with actual image path
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    encrypted_image_path = encrypt_image(image_path, msg, password)
    if encrypted_image_path:
        pas = input("Enter passcode for Decryption: ")
        if pas == password:
            decrypted_message = decrypt_image(encrypted_image_path, len(msg), pas)
            if decrypted_message:
                print("Decryption message:", decrypted_message)
        else:
            print("YOU ARE NOT AUTHORIZED")

if __name__ == "__main__":
    main()
