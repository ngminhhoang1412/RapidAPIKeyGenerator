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


def write_file(file, content, email):
    with open(file, 'a') as file:
        file.write(email + ':' + content + '\n')
