# Filename:  image_manipulation.py
from PIL import Image

def resize_image(image_path, new_width, new_height):
    try:
        img = Image.open(image_path)
        resized_img = img.resize((new_width, new_height))
        resized_img.save("resized_image.jpg")
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def rotate_image(image_path, degrees):
    try:
        img = Image.open(image_path)
        rotated_img = img.rotate(degrees)
        rotated_img.save("rotated_image.jpg")
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False