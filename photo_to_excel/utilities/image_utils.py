from PIL import Image


def get_images_data(image_list):
    _images_data = {}

    for image_path in image_list:
        img = Image.open(image_path)
        size = img.size

        _images_data[image_path] = {"size": size}

    return _images_data