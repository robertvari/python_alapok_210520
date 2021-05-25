import os


def check_path(path):
    return os.path.exists(path)


def get_images(folder_path):
    ext_list = [".jpg", ".jpeg"]

    file_list = [i for i in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, i))]
    return [os.path.join(folder_path, i) for i in file_list if os.path.splitext(i)[1].lower() in ext_list]