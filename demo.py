# import os
# from PIL import Image
#
# file = "0000982664.tif"
# img = Image.open(file)
# img.thumbnail((50, 50))
# img.save('jpgfile.jpg', 'JPEG')
#
from modules.database import CreateConnection

a = CreateConnection().get_last_n_records(3)

print(a)
