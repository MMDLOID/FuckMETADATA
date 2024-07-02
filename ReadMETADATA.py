from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(image_path):
    try:
        image = Image.open(image_path)
        
        # Extract EXIF data
        exif_data = image._getexif()
        
        if not exif_data:
            print("No EXIF metadata found.")
            return

        # Create a dictionary to store the metadata
        metadata = {}

        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            metadata[tag_name] = value

        # Print the metadata
        for tag_name, value in metadata.items():
            print(f"{tag_name}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask for the path to the image file
    image_path = input("Please enter the path to the image file: ")
    get_image_metadata(image_path)
