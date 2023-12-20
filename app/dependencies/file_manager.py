from app.config import settings
from app.services.file_manager import FileManager


def get_firmware_folder():
    return FileManager(upload_folder=settings.FIRMWARE_FOLDER)

