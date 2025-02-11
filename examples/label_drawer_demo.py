from src.file import retrieve_files

if __name__ == "__main__":
    datasets_path = r"datasets/train/images"
    label_path = r"datasets/train/labels"

    images = retrieve_files(datasets_path, extensions=["jpg"])
    annotations = retrieve_files(label_path, extensions=["txt"])

    print(len(images), len(annotations))
