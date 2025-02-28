import os
from rembg import remove
from PIL import Image

# Define input and output directories
input_folder = "preprocessed_images"
output_folder = "processed_images"

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def remove_background_from_folder():
    # Get list of images in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("No images found in the 'preprocessed_images' folder.")
        return

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file.replace('.jpg', '.png'))  # Ensure PNG format for transparency

        try:
            with open(input_path, "rb") as inp_file:
                input_image = inp_file.read()

            output_image = remove(input_image)

            with open(output_path, "wb") as out_file:
                out_file.write(output_image)

            print(f"Processed: {image_file} → {output_path}")

        except Exception as e:
            print(f"Error processing {image_file}: {e}")

if __name__ == "__main__":
    remove_background_from_folder()
    print("Background removal process completed!")

