import os

from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


def organize(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


print(organize('.txt'))


def organize_dir():
    for item in os.scandir():
        # we will skip is item is a dir
        if item.is_dir():
            continue

        # ------------------
        FILE_PATH = Path(item)
        FILE_TYPE = FILE_PATH.suffix.lower()
        DIRECTORY = organize(FILE_TYPE)
        DIRECTORY_PATH = Path(DIRECTORY)

        if not DIRECTORY_PATH.is_dir():
            DIRECTORY_PATH.mkdir()
        FILE_PATH.rename(DIRECTORY_PATH.joinpath(FILE_PATH))


organize_dir()
