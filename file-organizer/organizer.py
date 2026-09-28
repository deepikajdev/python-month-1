"""
File Organizer
A beginner-friendly file organization script that scans a directory,
groups files by extension, and moves them into organized folders.
"""

import os
import shutil

# Dictionary mapping folder names to known file extensions
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
}


def get_category(extension):
    """
    Return the category folder name based on the file extension.
    Defaults to 'Others' if the extension is unrecognized or missing.
    """
    ext_lower = extension.lower()
    for category, extensions in EXTENSION_MAP.items():
        if ext_lower in extensions:
            return category
    return "Others"


def organize_folder(folder_path):
    """
    Organize files inside folder_path into categorized subfolders.
    """
    # Validate that path exists and is a directory
    if not os.path.exists(folder_path):
        print(f"Error: The path '{folder_path}' does not exist.")
        return

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is a file, not a directory.")
        return

    # Category names created by this organizer
    reserved_folders = set(EXTENSION_MAP.keys())
    reserved_folders.add("Others")

    moved_counts = {}
    total_moved = 0

    print(f"\nScanning: {folder_path}...")

    # Iterate through each item in the directory
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip subdirectories (including our created category folders)
        if os.path.isdir(item_path):
            continue

        # Extract file extension (e.g., '.jpg')
        _, extension = os.path.splitext(item)
        category = get_category(extension)

        # Destination folder path
        destination_folder = os.path.join(folder_path, category)

        try:
            # Create destination folder if it doesn't already exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_path = os.path.join(destination_folder, item)

            # Move the file
            shutil.move(item_path, destination_path)
            print(f"Moved: {item} -> {category}/")

            moved_counts[category] = moved_counts.get(category, 0) + 1
            total_moved += 1

        except Exception as error:
            print(f"Failed to move '{item}': {error}")

    # Summary report
    print("\n" + "=" * 35)
    print("        ORGANIZATION SUMMARY        ")
    print("=" * 35)
    if total_moved == 0:
        print("No loose files found to organize.")
    else:
        for cat, count in moved_counts.items():
            print(f"  {cat}: {count} file(s)")
        print(f"\nTotal files organized: {total_moved}")
    print("=" * 35)


def main():
    """Main CLI entry point."""
    print("=" * 45)
    print("            FILE ORGANIZER CLI               ")
    print("=" * 45)
    print("Automatically sorts files into Images, Documents,")
    print("Videos, Music, and Others.\n")

    user_path = input("Enter the absolute path of the folder to organize: ").strip()

    # Remove enclosing quotes if user copied path with quotes
    user_path = user_path.strip("\"'")

    if not user_path:
        print("Path cannot be empty. Exiting.")
        return

    organize_folder(user_path)


if __name__ == "__main__":
    main()
