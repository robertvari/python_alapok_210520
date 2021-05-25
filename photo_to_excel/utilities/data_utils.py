from openpyxl import Workbook
import os


def save_images_data(folder_path, images_data):
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "Path"
    sheet["B1"] = "Dimensions"

    for index, file_path in enumerate(images_data):
        row = index + 3
        size = images_data[file_path]["size"]

        sheet[f"A{row}"] = file_path
        sheet[f"B{row}"] = f"{size[0]}x{size[1]}"

    excel_file = os.path.join(folder_path, "photo_data.xlsx")
    workbook.save(excel_file)