import os


def get_files(folder_path: str, ext: str = None, name_filter: str = None) -> list:
    assert os.path.exists(folder_path), f"Folder doesn't exist: {folder_path}"

    result = [i for i in os.listdir(folder_path)]
    if ext:
        filtered_result = []
        for i in result:
            file_name, _ext = os.path.splitext(i)

            if _ext.lower() == ext.lower():
                filtered_result.append(i)

        result = filtered_result

    if name_filter:
        # todo finis this tomorrow
        pass

    return result


def get_all_files(folder_path, file_list=[]) -> list:
    assert os.path.exists(folder_path), f"Folder doesn't exist: {folder_path}"

    all_content = [os.path.join(folder_path, i) for i in os.listdir(folder_path)]

    file_list += [i for i in all_content if os.path.isfile(i)]

    subfolders = [i for i in all_content if os.path.isdir(i)]
    for folder in subfolders:
        get_all_files(folder)

    return file_list