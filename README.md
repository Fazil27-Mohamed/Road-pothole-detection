# 🚧 Pothole Detection using YOLOv8

An AI-powered computer vision project that detects potholes from road images and videos using the YOLOv8 object detection model.

---

## 📖 Project Overview

This project automatically detects potholes from uploaded images and videos using a custom-trained YOLOv8 model.

The system is trained on a pothole dataset and predicts potholes by drawing bounding boxes around detected road damages.

This project can be useful for:

- 🛣️ Road Maintenance
- 🏙️ Smart Cities
- 🚗 Driver Assistance Systems
- 🤖 Autonomous Vehicles
- ⚠️ Road Safety Monitoring

---

## ✨ Features

- Detect potholes in images
- Detect potholes in videos
- Custom-trained YOLOv8 model
- High detection accuracy
- Bounding box visualization
- Responsive and attractive UI
- Supports multiple image and video formats

---

## 🛠️ Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```text
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
│   ├── script.js
│   └── images/
│
├── templates/
│   └── index.html
│
├── runs/
│
└── README.md
```

---

## 📊 Dataset

The model was trained using a custom pothole dataset.

### Dataset contains

- Road Images
- Potholes
- Bounding Box Annotations

### Annotation Format

```text
Class_ID
X_center
Y_center
Width
Height
```

---

## 🧠 Model Training

The project uses the **YOLOv8 Nano** model.

### Training Configuration

| Parameter | Value |
|-----------|--------|
| Model | YOLOv8n |
| Epochs | 50 |
| Image Size | 640 |
| Framework | Ultralytics |

### Training Code

```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
```

---

## 🖼️ Image Detection

```python
results = model(image)

annotated = results[0].plot()
```

The model detects potholes and draws bounding boxes with confidence scores.

---

## 🎥 Video Detection

The uploaded video is processed frame by frame.

Each frame is analyzed using the trained YOLOv8 model.

Detected potholes are marked with bounding boxes, and the processed frames are combined into a new output video.

---

## 📸 Sample Workflow

```text
Input Image / Video
          │
          ▼
YOLOv8 Detection
          │
          ▼
Bounding Boxes Generated
          │
          ▼
Output Image / Video
```

---

## 📈 Future Improvements

- Live webcam detection
- Drone-based pothole monitoring
- GPS location tracking
- Damage severity estimation
- Cloud deployment
- Mobile application
- Automatic maintenance report generation

---

## 🎯 Applications

- Smart City Projects
- Highway Monitoring
- Road Infrastructure Inspection
- Autonomous Driving
- Municipal Road Maintenance
- Accident Prevention Systems

---

## ✅ Advantages

- Fast Detection
- Lightweight Model
- High Accuracy
- Easy to Use
- Supports Images and Videos
- Real-Time Prediction

