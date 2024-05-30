import os
import uuid
import wget

def download_model():
    url = 'https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt'
    dest_path = 'models/yolov10/weights'
    os.makedirs(dest_path, exist_ok=True)
    wget.download(url, out=dest_path)


def generate_name():
    uuid_str = str(uuid.uuid4())

    return uuid_str

def save_upload_file(upload_file, save_folder='images'):
    os.makedirs(save_folder, exist_ok=True)
    if upload_file:
        new_filename = generate_name()
        save_path = os.path.join(save_folder, new_filename)
        with open(save_path, 'wb+') as f:
            data = upload_file.read()
            f.write(data)

        return save_path
    else:
        raise('Image not found.')
    
def delete_file(file_path):
    os.remove(file_path)