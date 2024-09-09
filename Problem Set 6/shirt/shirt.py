import sys
from PIL import Image, ImageOps
import os

def check_file_extension(in_file, out_file):
    extensions = ['.jpg', '.jpeg', '.png']

    # 获取文件拓展名
    ext1 = os.path.splitext(in_file)[1].lower()
    ext2 = os.path.splitext(out_file)[1].lower()

    if ext1 not in extensions or ext2 not in extensions :
        sys.exit("Invalid arguments")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    check_file_extension(in_file, out_file)

    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        people = Image.open(sys.argv[1])
        cropped_people = ImageOps.fit(image = people, size = size)
        cropped_people.paste(shirt, mask=shirt)
        cropped_people.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File Not Found")

if __name__ == "__main__":
    main()
