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
