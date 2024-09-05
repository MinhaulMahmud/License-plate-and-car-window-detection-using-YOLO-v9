# LicensePlate and Car Window detection using YOLOv8-seg
## YOLO segmentation based object detection

![YOLO](https://img.shields.io/badge/YOLO-v8-blue?style=flat-square) ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-4.x-blue?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-red?style=flat-square)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Performance](#performance)
- [Training the Model](#training-the-model)
- [Creating a Dataset YAML File](#creating-a-dataset-yaml-file)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The YOLO-Based Object Detection Project leverages a custom-trained YOLOv8m-seg model to detect License Plates and glass objects in images. The model adds bounding boxes and segmentations around detected objects. This project is optimized for mid-range hardware, ensuring efficient detection and smooth performance.

## Features

- **Real-time Object Detection and Segmentation:** Detects License Plates and glass objects.
- **Bounding Boxes & Segmentation:** Adds bounding boxes and segmentations around identified objects.
- **Optimized Performance:** Efficient for mid-range hardware configurations.
- **Detailed Results:** Displays inference times, object counts, and masks for each image.

## Requirements

- **Python** 3.11
- **OpenCV** 4.x
- **NumPy** 1.21+
- **Ultralytics YOLO** library (YOLOv8)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MinhaulMahmud/Licenseplate_and_car_window_detection_using_YOLOv8m-seg.git
   cd Licenseplate_and_car_window_detection_using_YOLOv8m-seg
   ```

2. **Install the required dependencies:**

   ```bash
   pip install opencv-python-headless numpy ultralytics
   ```

3. **Download the YOLOv8m-seg model:**

   Place the YOLOv8m-seg model file (`6path.pt`).

## Configuration

Edit the script to set the following paths:

- **Input Directory:** Location of the images to be processed.
- **Output Directory:** Folder to save images with bounding boxes and segmentations.
- **Model Path:** Path to the YOLOv8m-seg model (`6path.pt`).

## Usage

To run the object detection process:

```bash
python combined_det.py
```

Results will be saved in the `output/` directory, with bounding boxes and segmentation masks drawn on the images.

## Performance

The model used is the **YOLOv8m-seg** model, which provides balanced speed and accuracy for segmentation tasks.

### Model Metrics:

| Model        | Size (pixels) | mAPbox | mAPmask | Speed (CPU ONNX, ms) | Speed (A100 TensorRT, ms) | Params (M) | FLOPs (B) |
|--------------|---------------|--------|---------|-----------------------|---------------------------|------------|-----------|
| YOLOv8n-seg  | 640           | 36.7   | 30.5    | 96.1                  | 1.21                      | 3.4        | 12.6      |
| YOLOv8s-seg  | 640           | 44.6   | 36.8    | 155.7                 | 1.47                      | 11.8       | 42.6      |
| **YOLOv8m-seg**  | **640**           | **49.9**   | **40.8**    | **317.0**                 | **2.18**                      | **27.3**       | **110.2**     |
| YOLOv8l-seg  | 640           | 52.3   | 42.6    | 572.4                 | 2.79                      | 46.0       | 220.5     |
| YOLOv8x-seg  | 640           | 53.4   | 43.4    | 712.1                 | 4.02                      | 71.8       | 344.1     |

### Hardware Utilized:

- **Processor:** Intel i5 13th Generation
- **GPU:** RTX 3050 4GB

### Inference Time:

- **Speed:** Ranges from 72.7ms to 209.3ms depending on image complexity and resolution.


## Training the Model

1. **Annotate Data:** Use [LabelImg](https://github.com/tzutalin/labelImg) to annotate your images for object detection and segmentation.
2. **Train the Model:**

   ```bash
   yolo train data=your_data.yaml model=yolov8m-seg.pt epochs=100 imgsz=640
   ```

3. **Evaluate Performance:** Measure precision, recall, and mAP for the trained model.

## Creating a Dataset YAML File

To train your YOLOv8 model, you need to create a dataset YAML file that specifies the paths to your images and classes. Below is a sample YAML file:

```yaml
train: /path/to/your/train/images  # Path to training images
val: /path/to/your/val/images      # Path to validation images

# Number of classes in your dataset
nc: 2

# Class names
names: ['LicensePlate', 'Glass']
```

- **train:** The path to your training images folder.
- **val:** The path to your validation images folder.
- **nc:** The number of classes in your dataset.
- **names:** A list of class names in your dataset.

Ensure that the YAML file is correctly formatted and saved in your project directory. Then, you can use this YAML file during the training process.

## Project Structure

```bash
YOLO-Based-Object-Detection/
│
├── combined_det.py
├── test/
│   └── images/
│
├── output/
│
├── 6path.pt    # Your model
│
│
└── README.md
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- **Name:** Minhazul Mahmud
- **Email:** minhaz.oj@gmail.com
- **GitHub:** [Minhazul Mahmud](https://github.com/MinhaulMahmud)
- **LinkedIn:** [Minhazul Mahmud](https://www.linkedin.com/in/minhazul-mahmud-71702a29a/)
```
