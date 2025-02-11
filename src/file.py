import os


def get_files(folder_path: str) -> list[str] | None:
    """
    Retrieves a list of files in the specified folder.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        list[str]: List of file paths if the folder exists, or None if invalid.
    """
    if not os.path.isdir(folder_path):
        return None
    return [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file))
    ]


def is_valid_extension(file_path: str, extensions: list[str]) -> bool:
    """
    Checks if a file has a valid extension.

    Args:
        file_path (str): Path to the file.
        extensions (list[str]): List of valid extensions.

    Returns:
        bool: True if the file has a valid extension, False otherwise.
    """
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower().lstrip(".") in extensions


def parse_label_file(label_path: str) -> list[tuple[float, float, float, float, float]]:
    """
    Parses a YOLO format label file and extracts bounding box data.

    Args:
        label_path (str): Path to the label file.

    Returns:
        list[tuple]: List of bounding box data as (class_id, x_center, y_center, width, height).
    """
    bounding_boxes = []
    with open(label_path, "r") as label_file:
        for line in label_file:
            data = line.strip().split()
            bounding_boxes.append(tuple(map(float, data)))
    return bounding_boxes


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
    if not is_valid_extension(file_path, extensions):
        return False

    directory, _ = os.path.split(file_path)
    _, file_extension = os.path.splitext(file_path)

    # Generate new file name and path
    new_file_name = f"{new_name}-{counter}{file_extension}"
    new_file_path = os.path.join(directory, new_file_name)

    if os.path.exists(new_file_path):
        return False

    return _perform_rename(file_path, new_file_path)


def retrieve_files(folder_path: str, extensions: list[str]) -> list[str]:
    """
    Retrieves files from a folder that match the valid extensions.

    Args:
        folder_path (str): Path to the folder.
        extensions (list[str]): List of valid extensions.

    Returns:
        list[str]: List of files with valid extensions, or an empty list if none found.
    """
    files = get_files(folder_path)
    if not files:
        return []

    return [file for file in files if is_valid_extension(file, extensions)]


def _perform_rename(source: str, destination: str) -> bool:
    """
    Performs the actual renaming operation.

    Args:
        source (str): Current file path.
        destination (str): New file path.

    Returns:
        bool: True if the renaming was successful, False otherwise.
    """
    try:
        os.rename(source, destination)
        return True
    except Exception as e:
        return False
