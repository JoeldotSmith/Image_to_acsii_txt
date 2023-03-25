from PIL import Image

ASCII_CHAR = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = (height / width) / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def gray(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHAR[pixel//25] for pixel in pixels])
    return characters

def main(new_width=100):
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except:
        print(path, ", is not a valid pathname to an image.")

    new_image_data = pixel_to_ascii(gray(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    print(ascii_image)
    with open("/Users/joelsmith/Desktop/ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()
