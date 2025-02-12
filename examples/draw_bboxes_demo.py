import os

import src.yolo_utils as yutils
from src.file import parse_label_file, retrieve_files


def process_image_and_labels(
    image_path: str, label_path: str, output_folder: str
) -> None:
    """
    Processes an image and its corresponding label file, drawing bounding boxes and saving the result.

    Args:
        image_path (str): Path to the image file.
        label_path (str): Path to the label file.
        output_folder (str): Folder to save the processed image.
    """
    image = yutils.load_image(image_path)
    if image is None:
        return

    bounding_boxes = parse_label_file(label_path)

    img_height, img_width = image.shape[:2]

    for bbox in bounding_boxes:
        class_id, x_center, y_center, width, height = bbox
        pixel_bbox = yutils.yolo_to_opencv(
            x_center, y_center, width, height, img_width, img_height
        )
        yutils.draw_bounding_box(image, int(class_id), pixel_bbox)

    yutils.save_image(image, output_folder, image_path)


def process_dataset(images_folder: str, labels_folder: str, output_folder: str) -> None:
    """
    Processes a dataset of images and labels, drawing bounding boxes and saving the results.

    Args:
        images_folder (str): Path to the folder containing images.
        labels_folder (str): Path to the folder containing labels.
        output_folder (str): Path to the folder to save processed images.
    """
    images = retrieve_files(images_folder, extensions=["jpg"])
    annotations = retrieve_files(labels_folder, extensions=["txt"])

    # Match images and labels by name
    image_label_pairs = {
        os.path.splitext(os.path.basename(img))[0]: img for img in images
    }

    for label in annotations:
        label_name = os.path.splitext(os.path.basename(label))[0]
        if label_name in image_label_pairs:
            process_image_and_labels(
                image_label_pairs[label_name], label, output_folder
            )


if __name__ == "__main__":
    # Change these paths to your actual paths
    process_dataset(
        images_folder="datasets/train/images",
        labels_folder="datasets/train/labels",
        output_folder="datasets/train/output",
    )
