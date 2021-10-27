# -*- coding: utf-8 -*-
# -----------------------------
# The following program is for images processing
from PIL import Image, ImageFilter
from os import chdir, listdir
import os

chdir("E:/Project/Python_Projects/Test_Data/Images")
"""
# img = Image.open("4.4 pikachu.jpg")
img = Image.open("6.1 astro.jpg")

print("SIZE: ==> ", img.size)
print("FORMAT: ==> ", img.format )
print("MODE: ==> ", img.mode)

img.thumbnail((400, 400))
img.save("astro.jpg")
img.show()
"""
"""
# blured image : image flouté (IMageFilter.BLUR)

filtered_img = img.convert("L")
filtered_img.save("pickachu_grey.png", "png")
filtered_img.show()

filtered_resized_img = filtered_img.resize((300, 300))
filtered_resized_img.save("picka_resize.png", "png")
filtered_resized_img.show()

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("picka_crop.png", "png")
region.show()
"""
# ---------------------------------------------------------------
# Exercice JPEG to PNG Converter
# COnverts all images from a folder into JPEG to another folder -
# ---------------------------------------------------------------
# grab first and second argument
source_folder = "E:/Project/Python_Projects/Test_Data/Images"
chdir(source_folder)
output_folder = "E:/Project/Python_Projects/Test_Data/Images/new"

# check if the target folder exists (new/), if not create it
if os.path.exists(output_folder):
    pass
else:
    os.makedirs(output_folder)

# loop through images source folder
for filename in listdir(source_folder):
    if filename.endswith(".jpg"):
        img = Image.open(filename)
        src_file_path = os.path.abspath(filename)
        print(src_file_path)
        print("Converting {} ...".format(filename))
        clean_file = os.path.splitext(filename)[0]
        dest_file_path = output_folder + "/" + clean_file
        print(dest_file_path + ".png")

# Convert images to png & save them to the new folder
        img.save(dest_file_path + ".png", "png")
        print("Converting {} done !!!".format(filename))
    else:
        pass

chdir(output_folder)
print("\nDestination folder......\n")
input("......")
print(listdir())
