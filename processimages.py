from PIL import Image
from pathlib import Path

thumbnail_path = Path.cwd().joinpath('thumbnails')
if not thumbnail_path.exists():
    thumbnail_path.mkdir()

# Get images
raw_path = Path.cwd().joinpath('raw_images')
print(raw_path)
imfiles = raw_path.rglob("*.JPG")

# process images
for img in imfiles:
    print(img)
    my_image = Image.open(img)

    # create thumbnails
    my_image.thumbnail((120,120))

    # save
    thumbnail_output = thumbnail_path.joinpath(img.name)
    my_image.save(thumbnail_output)


# Output images