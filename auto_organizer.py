import shutil
from pathlib import Path
import logging

# Define constants
LOG_FILENAME = 'desktop_organizer.log'
SCRIPT_FILENAME = Path(__file__).name  # Dynamically get the script's name
EXCLUDE_FILES = [LOG_FILENAME, SCRIPT_FILENAME]


logging.basicConfig(
    filename='desktop_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define the desktop path
desktop_path = Path.cwd()

# Define target folders and associated file extensions
file_categories = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".ppt", ".doc", ".xls"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
    # Add more categories and extensions as needed
}


def create_folders(categories, base_path):
    for folder in categories.keys():
        folder_path = base_path / folder
        if not folder_path.exists():
            folder_path.mkdir()
            logging.info(f"Created folder: {folder_path}")



def get_unique_filename(target_folder, file):
    ii = 1
    new_name = file.name
    target_path = target_folder / new_name
    while target_path.exists():
        new_name = f"{file.stem}_{ii}{file.suffix}"
        target_path = target_folder / new_name
        ii += 1
    return new_name


def organize_files(categories, base_path):
    for item in base_path.iterdir():
        if item.is_file():
            if item.name in EXCLUDE_FILES:
                logging.info(f"Skipping excluded file: {item.name}")
                continue

            moved = False
            for category, extensions in categories.items():
                if item.suffix.lower() in extensions:
                    target_folder = base_path / category
                    new_name = get_unique_filename(target_folder, item)
                    shutil.move(str(item), target_folder / new_name)
                    logging.info(f"Moved: {item.name} --> {target_folder / new_name}")
                    moved = True
                    break

            if not moved:
                target_folder = base_path / "Others"
                new_name = get_unique_filename(target_folder, item)
                shutil.move(str(item), target_folder / new_name)
                logging.info(f"Moved: {item.name} --> {target_folder / new_name}")


def main():
    create_folders(file_categories, desktop_path)
    organize_files(file_categories, desktop_path)


if __name__ == "__main__":
    main()
