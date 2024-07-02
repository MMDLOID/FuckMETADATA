import os
from PIL import Image

def remove_metadata_from_images():
    #get current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    #list all file
    files = os.listdir(current_directory)

    #loop all file
    for file in files:
        #check if IMG
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(current_directory, file)

            try:
                #Open IMG
                with Image.open(file_path) as img:
                    #Save IMG with no METADATA
                    img_data = list(img.getdata())
                    img_no_metadata = Image.new(img.mode, img.size)
                    img_no_metadata.putdata(img_data)
                    img_no_metadata.save(file_path)

                print(f"Metadata removed from: {file}")

            except Exception as e:
                print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    remove_metadata_from_images()
