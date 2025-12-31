import rawpy
import imageio
import os

def convert_raw_to_jpg(filename):
    try:
        print(f"Converting {filename}...")
        with rawpy.imread(filename) as raw:
            rgb = raw.postprocess()
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            imageio.imsave(new_filename, rgb)
            print(f"Saved {new_filename}")
            return new_filename
    except Exception as e:
        print(f"Failed to convert {filename}: {e}")
        return None

files_to_convert = [
    "DSC01462.ARW",
    "DSC01463.ARW",
    "IMG_9535.CR3",
    "IMG_9554 (1).CR3"
]

converted_files = []
for file in files_to_convert:
    if os.path.exists(file):
        result = convert_raw_to_jpg(file)
        if result:
            converted_files.append(result)
    else:
        print(f"File not found: {file}")
