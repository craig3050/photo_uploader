import os
import shutil
from PIL import Image
import requests
import json


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "creds.json"

def compress_pictures(picture_path):

    print(f"compressing image {picture_path}")
    try:
        with Image.open(picture_path) as image_to_convert:
            image_to_convert.save(picture_path, optimize=True, quality=90)
    except IOError:
        print("Cannot convert this file...")




def upload_picture(picture_path):
    pass





if __name__ == '__main__':
    folder_path = input("Please enter the folder path of the files you wish to upload: ")

# List the folders
    for item in os.listdir(folder_path):
        sub_folder_path = ""
        sub_folder_path = os.path.join(folder_path, item)

# List the files
        for file in os.listdir(sub_folder_path):
            #Send file for compression
            compress_pictures(os.path.join(sub_folder_path, file))

            #upload file to google photos


