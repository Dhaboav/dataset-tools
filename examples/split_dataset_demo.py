import os

import src.file as file


def run(label_path: str, output_folder: str):
    """
    Run the dataset splitting and saving process.

    Args:
        label_path (str): Path to the directory containing label files.
        output_folder (str): Path to the folder to save output files.
    """
    file_names = file.get_files_names(label_path)
    train_set, val_set, test_set = file.split_dataset(file_names)

    file.save_to_file(train_set, os.path.join(output_folder, "train.txt"))
    file.save_to_file(val_set, os.path.join(output_folder, "val.txt"))
    file.save_to_file(test_set, os.path.join(output_folder, "test.txt"))

    total = len(file_names)
    train = len(train_set)
    valid = len(val_set)
    test = len(test_set)
    print(f"Total: {total}, train: {train}, valid: {valid}, test: {test}")


if __name__ == "__main__":
    # Change these paths to your actual paths
    run(label_path="datasets/train/labels", output_folder="datasets/split")
