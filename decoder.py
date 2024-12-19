import qrcode
import cv2
import numpy as np


def generate_qr_code(data, file_name):
    """
    Generate a QR code for the given data and save it as an image file.

    Args:
        data (str): The information to encode into the QR code.
        file_name (str): The name of the file to save the QR code.
    """
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code, 1 is the smallest
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a file
    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")


def decode_qr_code(file_name):
    """
    Decode a QR code from an image file and retrieve the embedded data.

    Args:
        file_name (str): The name of the file containing the QR code.

    Returns:
        str: The data embedded in the QR code.
    """
    # Read the image using OpenCV
    image = cv2.imread(file_name)

    # Initialize the QR code detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    data, _, _ = detector.detectAndDecode(image)

    if data:
        print(f"Decoded Data: {data}")
    else:
        print("No QR code detected or the code is unreadable.")

    return data


def main():
    while True:
        print("\nQR Code Encoder/Decoder")
        print("1. Generate QR Code")
        print("2. Decode QR Code")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter the data to encode: ")
            file_name = input("Enter the file name to save the QR code (e.g.,'abcqrcode.png'): ")
            generate_qr_code(data, file_name)
        elif choice == "2":
            file_name = input("Enter the file name of the QR code to decode: ")
            decode_qr_code(file_name)
        elif choice == "3":
            print("Exiting QR Code Encoder/Decoder.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
