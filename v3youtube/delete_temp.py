import os
import common.constants as Constant


def delete_temp():
    for root, _, files in os.walk(Constant.TEMP_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except (Exception, ValueError):
                pass
