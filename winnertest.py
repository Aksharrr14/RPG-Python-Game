from PIL import Image

def resize_image(input_path, output_path, new_size=(300, 300)):
    """
    Resize an image.

    Parameters:
    - input_path: The path to the input image.
    - output_path: The path to save the resized image.
    - new_size: Tuple specifying the new size (width, height). Default is (300, 300).
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize(new_size, Image.ANTIALIAS)
            # Save the resized image
            resized_img.save(output_path)
            print(f"Image resized and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_image_path = "./img/video-game-winner-vector.png"
output_image_path = "./img/winnerphotobig.png"
resize_image(input_image_path, output_image_path, new_size=(1850, 1080))
