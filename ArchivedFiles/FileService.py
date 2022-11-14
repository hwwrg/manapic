from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('Capture001.png')
info = img._getexif()
print(info)


# for k, v in info.items():
#     nice = TAGS.get(k, k)
#     # print('%s (%s) = %s' % (nice, k, v))