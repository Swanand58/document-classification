from PIL import Image


def check_file_ext(filename):
    # assert isinstance(filename, str)
    allowed_extensions = ['png', 'jpg', 'jpeg', 'tif']
    return True if filename.rsplit('.')[-1] in allowed_extensions else False


def generate_thumbnail(image_path, size):
    assert isinstance(size, tuple)

    image = Image.open(image_path)
    filename = image_path.split('/')[-1].split('.')[0]
    image.thumbnail(size)
    image.save('./static/thumbnails/{}.jpg'.format(filename), 'JPEG')
