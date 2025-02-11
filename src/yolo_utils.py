import os

import cv2

from .logger import log_message


def draw_bounding_box(
    image: cv2.Mat, class_id: int, bbox: tuple[int, int, int, int]
) -> None:
    """
    Draws a bounding box with a label on an image, using a color based on the class ID.

    Args:
        image (cv2.Mat): The image to draw on.
        bbox (tuple[int, int, int, int]): The bounding box coordinates (x_min, y_min, x_max, y_max).
        class_id (int): The class ID to display.
    """
    x_min, y_min, x_max, y_max = bbox
    color = _get_color_for_class(class_id)
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)


def load_image(image_path: str) -> cv2.Mat | None:
    """
    Loads an image from the given path.

    Args:
        image_path (str): Path to the image file.

    Returns:
        cv2.Mat | None: Loaded image or None if the image couldn't be loaded.
    """
    image = cv2.imread(image_path)
    if image is None:
        log_message("No image", "ERROR")
    return image


def save_image(image: cv2.Mat, output_folder: str, image_path: str):
    """
    Saves the image to the specified output folder.

    Args:
        image (cv2.Mat): The image to save.
        output_folder (str): Folder to save the image.
        image_path (str): Original path of the image to extract the file name.
    """
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_path, image)
    log_message(f"Success {image_path}")


def yolo_to_opencv(
    center_x: float,
    center_y: float,
    bbox_width: float,
    bbox_height: float,
    img_width: int,
    img_height: int,
) -> tuple[int, int, int, int]:
    """
    Convert YOLO format bounding box to OpenCV format.

    Args:
        center_x (float): bbox x coordinate.
        center_y (float): bbox y coordinate.
        bbox_width (float): bbox width.
        bbox_height (float): bbox height.
        img_width (int): img width size dimension.
        img_height (int): img height size dimension.

    Returns:
        tuple[int, int, int, int]: Bounding box in opencv format.
    """

    half_width, half_height = bbox_width / 2, bbox_height / 2
    x_min = int((center_x - half_width) * img_width)
    y_min = int((center_y - half_height) * img_height)
    x_max = int((center_x + half_width) * img_width)
    y_max = int((center_y + half_height) * img_height)

    return x_min, y_min, x_max, y_max


def _get_color_for_class(class_id: int) -> tuple[int, int, int]:
    """
    Generates a unique color for a given class ID.

    Args:
        class_id (int): The class ID.

    Returns:
        tuple[int, int, int]: A color in BGR format.
    """
    r = (class_id * 37) % 256
    g = (class_id * 73) % 256
    b = (class_id * 17) % 256
    return (b, g, r)
