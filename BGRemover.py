from rembg import remove
from PIL import Image

input_path = r'D:\Study\Projects\EtoE test\data\IMG_8752.JPG'
output_path = r'data\output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)