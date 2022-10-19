from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('050.JPG')
info = img._getexif()
print(info[36867])

for k, v in info.items():
    nice = TAGS.get(k, k)
    # print('%s (%s) = %s' % (nice, k, v))