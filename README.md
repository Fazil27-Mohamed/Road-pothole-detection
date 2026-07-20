🚧 Pothole Detection using YOLOv8
📌 Project Overview

Pothole Detection using YOLOv8 is an AI-based computer vision project that automatically detects potholes from road images and videos. The system is trained on a custom pothole dataset using the YOLOv8 object detection model. A Flask web application provides an interactive interface where users can upload images or videos and instantly visualize detected potholes.

This project can be used for road maintenance, smart city applications, autonomous vehicles, and accident prevention systems.

🚀 Features
Detect potholes from images
Detect potholes from videos
Real-time object detection using YOLOv8
Interactive Flask web interface
Upload images and videos
Displays bounding boxes around potholes
Supports multiple file formats
Attractive and responsive UI
🛠️ Technologies Used
Python
YOLOv8 (Ultralytics)
Flask
OpenCV
HTML5
CSS3
📂 Project Structure
Pothole-Detection/
│
├── app.py
├── best.pt
├── requirements.txt
│
├── static/
│   ├── uploads/
│   ├── results/
│   ├── style.css
│   └── images/
│
├── templates/
│   └── index.html
│
├── runs/
│
└── README.md
📊 Dataset

The model is trained on a custom pothole dataset.

Dataset contains:

Road Images
Potholes
Bounding Box Annotations

Annotation Format:

YOLO Format

Class_ID
X_center
Y_center
Width
Height
🧠 Model Training

YOLOv8 Nano model was used.

Training Parameters

Model : YOLOv8n

Epochs : 50

Image Size : 640

Batch Size : Default

Framework : Ultralytics

Training Command

from ultralytics import YOLO

model = YOLO("yolo26n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
🖼️ Image Detection
results = model(image)

annotated = results[0].plot()

Detected image is displayed with bounding boxes around potholes.

🎥 Video Detection

The uploaded video is processed frame by frame.

Each frame is passed to the trained YOLO model.

Detected frames are written into a new output video.

Finally, the processed video is displayed on the web page.

🌐 Flask Web Application

The application provides:

Image Upload
Video Upload
Detection Result
Output Preview
Download Option
