from PIL import Image
from pathlib import Path

# Dictionary to save filenames, paths and thumbnail paths to
image_data={}


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

    # do some fancy image manipulation
    
    # create thumbnails
    my_image.thumbnail((120,120))

    # save
    thumbnail_output = thumbnail_path.joinpath(img.name)
    my_image.save(thumbnail_output)

    # Add to image dictionary
    image_data[img.name] = ( str(img.name), 
                            str(thumbnail_output),
                            str(img) )
                                 

# Output images

# create html list
html = """<!DOCTYPE html>
<html lang="en"
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Gallery</title>
    <link rel="stylesheet" href="style.css">
</head>
<style>
img {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 5px;
    width: 150px;
}
img:hover {
    box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
}
</style>
<body>
    
    <h2>Thumbnail Image</h2>
    <p>Click on the image to enlarge it.</p>"""

footer = """</body>
</html>"""

for key, i in image_data.items():
    image_name = i[0]
    thumbnail_path = i[1] #This is a bit dicey
    source_path = i[2]


    html += f"""<a target="_blank" href="{source_path}">
        <img src="{thumbnail_path}" alt="Forest">
    </a>"""

html += footer

with open(Path.cwd().joinpath('index.html'), "w") as my_outputfile:
    my_outputfile.write(html)