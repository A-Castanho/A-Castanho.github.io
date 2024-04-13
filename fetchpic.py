import os
from PIL import Image

def generate_image_list(folder_path):
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                caption = os.path.splitext(filename)[0].replace("_", " ").upper()  # Modify this line for custom captions
                image_list.append({
                    "image_path": image_path,
                    "caption": caption
                })
    return image_list

if __name__ == "__main__":
    folder_path = input("Enter the path to the gallery folder: ")
    if not os.path.isdir(folder_path):
        print("Error: The specified path does not exist or is not a directory.")
    else:
        image_list = generate_image_list(folder_path)
        print("images:")
        for image in image_list:
            print(" - image_path:", image["image_path"])
            print("   caption:", image["caption"])
            print("   copyright: © Alina Castanho")
