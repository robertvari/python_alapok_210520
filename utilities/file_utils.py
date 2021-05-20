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