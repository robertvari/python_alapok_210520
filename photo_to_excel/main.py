from utilities import image_utils, data_utils, file_utils


def main():
    folder_path = r"C:\Work\_PythonSuli\python_alapozo\photos"
    assert file_utils.check_path(folder_path), "Folder does not exist."

    images = file_utils.get_images(folder_path)

    assert images, "Folder does not contain images."

    images_data = image_utils.get_images_data(images)

    data_utils.save_images_data(folder_path, images_data)


if __name__ == '__main__':
    main()