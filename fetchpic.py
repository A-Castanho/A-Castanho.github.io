import os
from PIL import Image
import re

def generate_image_list(folder_name):
    image_list = []
    folder_path = os.path.join("gallery", "archive", folder_name)
    if not os.path.isdir(folder_path):
        print(f"Error: The specified folder '{folder_name}' does not exist.")
        return []

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join("/gallery/archive", folder_name, filename).replace("\\", "/")
            with Image.open(os.path.join(folder_path, filename)) as img:
                caption = os.path.splitext(filename)[0].replace("_", " ").upper()  # Modify this line for custom captions
                image_list.append({
                    "image_path": image_path,
                    "caption": caption
                })
    return image_list

def update_index_html(html_path, image_list):
    with open(html_path, "r") as file:
        html_content = file.read()

    # Find existing YAML front matter
    yaml_pattern = r"(---\s*\n)(.*?)(\n\s*---)"
    match = re.search(yaml_pattern, html_content, re.DOTALL)
    if match:
        start_yaml, existing_yaml, end_yaml = match.groups()
        updated_yaml = existing_yaml.strip() + "\n"  # Preserve existing YAML content

        # Update images section
        images_section = "\n".join([
            f"- image_path: {image['image_path']}\n  caption: {image['caption']}\n  copyright: © Alina Castanho"
            for image in image_list
        ])
        updated_yaml += f"\n{images_section}\n"

        updated_html_content = f"{start_yaml}{updated_yaml}{end_yaml}"

        # Preserve the remaining HTML content after YAML
        html_content_after_yaml = html_content.split(end_yaml, 1)[-1]
        updated_html_content += html_content_after_yaml
    else:
        print("Error: Unable to locate YAML front matter in the HTML file.")
        return

    with open(html_path, "w") as file:
        file.write(updated_html_content)
        print("index.html updated successfully.")

if __name__ == "__main__":
    folder_name = input("Enter the name of the folder inside 'archive' (e.g., animals): ")
    index_html_path = os.path.join("gallery", folder_name, "index.html")
    if not os.path.isfile(index_html_path):
        print("Error: The index.html file does not exist.")
    else:
        image_list = generate_image_list(folder_name)
        update_index_html(index_html_path, image_list)
