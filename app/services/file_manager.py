import os

from fastapi import UploadFile

from app.exceptions.exceptions import FileNotSavedException


class FileManager:
    def __init__(self, upload_folder: str) -> None:
        self.upload_folder = upload_folder

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

    async def save_uploaded_file(self, file: UploadFile) -> str:
        try:
            file_path = os.path.join(self.upload_folder, file.filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
        except Exception:
            raise FileNotSavedException

        return file_path
