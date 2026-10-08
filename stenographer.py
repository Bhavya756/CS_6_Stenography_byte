from PIL import Image
import os

SUPPORTED_FORMATS = [".png", ".bmp"]
DELIMITER = "###END###"


def calculate_capacity(image):
    """Return approximate maximum message capacity in characters."""
    width, height = image.size
    total_bits = width * height * 3
    usable_bytes = total_bits // 8
    return max(0, usable_bytes - len(DELIMITER))


def hide_message(input_image, output_image, message):
    """Hide a text message inside an image using LSB steganography."""

    extension = os.path.splitext(input_image)[1].lower()

    if extension not in SUPPORTED_FORMATS:
        print("Error: Unsupported image format.")
        print("Supported formats: PNG and BMP")
        return

    try:
        image = Image.open(input_image).convert("RGB")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    capacity = calculate_capacity(image)

    if len(message) > capacity:
        print(f"Error: Message is too large.")
        print(f"Maximum capacity: {capacity} characters")
        print(f"Your message: {len(message)} characters")
        return

    message = message + DELIMITER

    binary_message = ''.join(format(ord(char), '08b') for char in message)

    pixels = list(image.getdata())
    new_pixels = []

    bit_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)

        for channel in range(3):
            if bit_index < len(binary_message):
                new_pixel[channel] = (
                    (new_pixel[channel] & ~1)
                    | int(binary_message[bit_index])
                )
                bit_index += 1

        new_pixels.append(tuple(new_pixel))

    image.putdata(new_pixels)
    image.save(output_image)

    print("\nMessage successfully hidden!")
    print(f"Cover Image : {input_image}")
    print(f"Stego Image : {output_image}")
    print(f"Message Size: {len(message) - len(DELIMITER)} characters")
    print(f"Capacity    : {capacity} characters")


def extract_message(stego_image):
    """Extract a hidden message from a stego image."""

    extension = os.path.splitext(stego_image)[1].lower()

    if extension not in SUPPORTED_FORMATS:
        print("Error: Unsupported image format.")
        print("Supported formats: PNG and BMP")
        return

    try:
        image = Image.open(stego_image).convert("RGB")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    binary_data = ""

    for pixel in image.getdata():
        for channel in pixel:
            binary_data += str(channel & 1)

    extracted_text = ""

    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i + 8]

        if len(byte) < 8:
            break

        character = chr(int(byte, 2))
        extracted_text += character

        if extracted_text.endswith(DELIMITER):
            message = extracted_text[:-len(DELIMITER)]

            print("\nMessage successfully extracted!")
            print("--------------------------------")
            print("Hidden Message:")
            print(message)
            print("--------------------------------")
            return message

    print("\nNo hidden message found.")
    return None


def main():
    print("=" * 55)
    print("       IMAGE STEGANOGRAPHY UTILITY")
    print("       Hide & Extract Text in Image")
    print("=" * 55)

    while True:
        print("\nChoose an option:")
        print("1. Hide message")
        print("2. Extract message")
        print("3. Check image capacity")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            input_image = input("Enter cover image path: ").strip()
            output_image = input("Enter output stego image path: ").strip()
            message = input("Enter message to hide: ")

            hide_message(input_image, output_image, message)

        elif choice == "2":
            stego_image = input("Enter stego image path: ").strip()
            extract_message(stego_image)

        elif choice == "3":
            image_path = input("Enter image path: ").strip()

            try:
                image = Image.open(image_path)
                capacity = calculate_capacity(image)

                print("\nImage Capacity")
                print("----------------")
                print(f"Image Size : {image.size[0]} x {image.size[1]}")
                print(f"Capacity   : approximately {capacity} characters")

            except Exception as e:
                print(f"Error opening image: {e}")

        elif choice == "4":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()