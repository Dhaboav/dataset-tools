<br />
<div align="center">
<h3 align="center">dataset-tools</h3>

  <p align="center">
    A modular utility toolkit for managing datasets in machine learning and AI applications
  </p>
</div>

---

### Overview

`dataset-tools` is a modular utility toolkit for managing datasets in machine learning and AI applications. It simplifies common tasks such as:

- Converting labels between formats (e.g., YOLO TXT.).
- Visualizing bounding boxes on images from annotation files.
- Renaming and organizing dataset files.

`Tech` used in this repository:
- `isort` and `black` keep the code consistent and clean.
- `OpenCV` handles computer vision tasks.

---

### Installation Guide

Follow these steps to set up the project locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Dhaboav/dataset-tools.git
    ```


2. **Install Python dependencies:**

    Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```
    
---

### Examples

If you want to see how to use specific functions, navigate to the `examples` folder:

- **`draw_bboxes_demo.py`**: Demonstrates how to draw bounding boxes from YOLO TXT format annotations onto images using OpenCV and save the resulting images.

---

### Troubleshooting

#### Resolving Module Import Errors in VSCode
To fix **module import errors** in the `examples` folder, set `PYTHONPATH` in your VSCode settings so Python recognizes the project's root directory.

1. Open `Preferences: Open User Settings (JSON)` via `Ctrl+Shift+P` in VSCode.

2. Add this configuration:

   ```json
   {
       "terminal.integrated.env.windows": {
           "PYTHONPATH": "${workspaceFolder}"
       }
   }
