from PIL import Image


def process_image(image_path, output_path, key):
    try:
        # Open image
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size

        # Apply XOR operation to each pixel
        for x in range(width):
            for y in range(height):
                current_pixel = pixels[x, y]

                # Handle RGB or RGBA
                if len(current_pixel) >= 3:
                    r, g, b = current_pixel[:3]

                    # XOR with the key (same operation works for encryption and decryption)
                    r ^= key
                    g ^= key
                    b ^= key

                    if len(current_pixel) == 4:
                        a = current_pixel[3]
                        pixels[x, y] = (r, g, b, a)
                    else:
                        pixels[x, y] = (r, g, b)

        # Save processed image
        img.save(output_path)
        print(f"Success! Image saved at: {output_path}")

    except Exception as e:
        print(f"Error: {e}. Please check the file path.")


def main():
    print("--- Image Encryption Tool (Pixel Manipulation) ---")

    mode = input("What would you like to do? (encrypt/decrypt): ").lower().strip()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid choice!")
        return

    input_path = input("Input image path/name (e.g., photo.jpg): ")
    output_path = input("Output image name (e.g., encrypted.jpg): ")

    try:
        key = int(input("Encryption Key (an integer between 1 and 255): "))
        if not (1 <= key <= 255):
            print("Key must be between 1 and 255.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    process_image(input_path, output_path, key)


if __name__ == "__main__":
    main()

