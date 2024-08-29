## Overview

This repository contains the code and resources for a YOLO-based object detection project specifically focused on detecting LicensePlates and glass objects in images. The project uses a custom-trained YOLO v9 model to accurately identify these objects and draw bounding boxes around them. The model is optimized to work efficiently on mid-range hardware, including PCs with specifications such as an Intel i5 13th generation processor and an RTX 3050 4GB GPU.

## Features

- **Object Detection:** Detects LicensePlates and glass objects in images.
- **Bounding Box Drawing:** Automatically draws bounding boxes around detected objects.
- **Performance Optimization:** Tailored to run efficiently on mid-range hardware.
- **Detailed Output Information:** Provides insights into the detection process, including inference time and object count per image.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Ultralytics YOLO library

You can install the necessary dependencies using the following command:

```bash
pip install opencv-python-headless numpy ultralytics
```

### Cloning the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Running the Code

To run the object detection script on a set of images, simply place your images in the `test2` directory and run the following command:

```bash
python your_script_name.py
```

The processed images with bounding boxes will be saved in the `output` directory.

## Model Training

### Dataset Preparation

To train a YOLO v9 model for detecting LicensePlates and glass objects, you'll need a well-labeled dataset with images containing these objects. The dataset should be split into training, validation, and test sets.

### Training the Model

1. **Annotation:** Use tools like LabelImg to annotate your dataset. Ensure that each object is correctly labeled as either `LicensePlate` or `glass`.
2. **Model Configuration:** Modify the YOLO v9 configuration file to fit your dataset, specifying the number of classes (in this case, 2).
3. **Training:** Train the model using the YOLO library. An example command might look like this:

```bash
yolo train data=your_data.yaml model=yolov9.pt epochs=100 imgsz=640
```

4. **Hyperparameter Tuning:** Experiment with learning rates, batch sizes, and other hyperparameters to optimize performance.

### Evaluating Model Performance

After training, evaluate your model's performance using precision, recall, and mAP (mean Average Precision) metrics. These can be visualized using graph charts to analyze the model's accuracy and efficiency across different object types and scenarios.

## Performance Insights

### Hardware Utilization

The model is optimized to utilize the full potential of mid-range GPUs like the RTX 3050. With an Intel i5 13th generation processor and 4GB of VRAM, the model delivers satisfactory inference times across various image resolutions, as shown in the output logs:

- **Inference Time:** Ranges between 72.7ms and 209.3ms depending on image size and object count.
- **Postprocessing Time:** Efficient postprocessing ensures minimal delays after inference, crucial for real-time applications.

## Conclusion

This project demonstrates the potential of custom-trained YOLO models in specialized object detection tasks, optimized for mid-range hardware. With proper training and configuration, similar models can be adapted to a wide range of applications in various industries.

Feel free to fork this repository, experiment with the model, and contribute back with your enhancements!

---

### Additional Resources

- [YOLO Official Documentation](https://docs.ultralytics.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [LabelImg Annotation Tool](https://github.com/tzutalin/labelImg)

---

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details. 

---

By following the steps and insights provided, you can effectively train and deploy YOLO-based models for object detection tasks, leveraging the power of modern hardware configurations.