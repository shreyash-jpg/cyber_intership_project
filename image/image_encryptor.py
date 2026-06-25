from PIL import Image

def process_image(image_path, output_path, key):
    try:
        # Image open karein
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size

        # Har ek pixel par XOR operation apply karein
        for x in range(width):
            for y in range(height):
                current_pixel = pixels[x, y]
                
                # Check agar image RGB hai ya RGBA
                if len(current_pixel) >= 3:
                    r, g, b = current_pixel[:3]
                    # Key ke sath XOR operation (Yahi encryption aur decryption dono ka kaam karega)
                    r ^= key
                    g ^= key
                    b ^= key
                    
                    if len(current_pixel) == 4:
                        a = current_pixel[3]
                        pixels[x, y] = (r, g, b, a)
                    else:
                        pixels[x, y] = (r, g, b)

        # Processed image ko save karein
        img.save(output_path)
        print(f"Success! Image saved at: {output_path}")
        
    except Exception as e:
        print(f"Error: {e}. Please check the file path.")

def main():
    print("--- Image Encryption Tool (Pixel Manipulation) ---")
    
    mode = input("Kya karna chahte ho? (encrypt/decrypt): ").lower().strip()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid choice!")
        return
        
    input_path = input("Input image ka path/naam dalo (e.g., photo.jpg): ")
    output_path = input("Output image ka naam kya rakhna hai (e.g., encrypted.jpg): ")
    
    try:
        key = int(input("Encryption Key (1-255 ke beech koi number): "))
        if not (1 <= key <= 255):
            print("Key 1 aur 255 ke beech honi chahiye!")
            return
    except ValueError:
        print("Valid number dalo!")
        return

    process_image(input_path, output_path, key)

if __name__ == "__main__":
    main()