import cv2

from src.label_drawer import yolo_to_opencv

if __name__ == "__main__":
    datasets_path = (
        r"datasets\train\images\data-1_png.rf.f87531b8bf3c3e204809be92c509f0a8.jpg"
    )
    # Load the image
    image = cv2.imread(datasets_path)

    x, y, bboxw, bboxh = 0.18125, 0.334375, 0.058333333333333334, 0.10104166666666667

    # Get dimensions
    image_height, image_width = image.shape[:2]
    x_min, y_min, x_max, y_max = yolo_to_opencv(
        x, y, bboxw, bboxh, image_width, image_height
    )
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
    cv2.imshow("t", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(x_min, y_min)
