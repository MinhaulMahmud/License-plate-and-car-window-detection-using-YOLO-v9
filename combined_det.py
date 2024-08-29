import os
import cv2
import numpy as np
from ultralytics import YOLO

def detect_and_draw_boxes(image_path, output_path):
    # Read the input image
    frame = cv2.imread(image_path)
    H, W, _ = frame.shape

    # Detect objects in the image
    results = model(frame)[0]

    # Iterate over detected objects
    for i, result in enumerate(results.boxes.data.tolist()):
        x1, y1, x2, y2, score, class_id = result
        class_name = results.names[int(class_id)]

        if score > threshold and class_name in ['glass', 'LicensePlate']:
            # Draw bounding box around the detected object
            color = (0, 255, 0)  # Green color for bounding box
            thickness = 2  # Thickness of bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)

            # Put the class name and score on the bounding box
            label = f"{class_name}: {score:.2f}"
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

    # Save the resulting image with bounding boxes
    cv2.imwrite(output_path, frame)
    print(f"Resulting image with bounding boxes saved as {output_path}")

def process_images(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all images in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            detect_and_draw_boxes(image_path, output_path)

# Path to the input directory containing the images
input_dir = os.path.join('.', 'test', '')

# Path to the output directory where results will be saved
output_dir = os.path.join('.', 'output')

# Path to the YOLO model
model_path = os.path.join('.', '6path.pt')

# Load the YOLO model
model = YOLO(model_path)

# Threshold for object detection
threshold = 0.3

# Process images in the input directory
process_images(input_dir, output_dir)
