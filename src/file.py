import os


def rename_file(
    file_path: str, new_name: str, extensions: list[str], counter: int = 0
) -> bool:
    """
    Renames a file to a new name with a counter, if it matches the specified extensions.

    Args:
        file_path (str): Full path of the file to rename.
        new_name (str): Base name for the renamed file.
        extensions (list[str]): Valid file extensions (case-insensitive).
        counter (int, optional): Counter to append to the new file name. Defaults to 0.

    Returns:
        bool: True if the file was successfully renamed, False otherwise.
    """
    directory, file_name = os.path.split(file_path)
    _, file_extension = os.path.splitext(file_name)

    # Check for valid file extension
    if file_extension.lower().lstrip(".") not in extensions:
        return False

    # Generate new file name and path
    new_file_name = f"{new_name}-{counter}{file_extension}"
    new_file_path = os.path.join(directory, new_file_name)

    # Skip if the new file already exists
    if os.path.exists(new_file_path):
        return False

    os.rename(file_path, new_file_path)
    return True


def get_files(folder_path: str) -> list[str] | None:
    """
    Retrieves a list of files in the specified folder.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        list[str] | None: List of file paths if the folder exists, or None if invalid.
    """
    if not os.path.isdir(folder_path):
        return None
    return [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file))
    ]
