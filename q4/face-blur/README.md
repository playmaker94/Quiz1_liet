#  Face Blurring in Live Video Feed using YOLOv8 and OpenCV

This project captures a live video feed from a webcam (or CCTV stream), detects faces in real-time using the YOLOv8 face detection model, applies a strong blur to each detected face for privacy protection, and displays the processed video. It also allows the user to save video clips on demand.

---

##  Features

- Real-time face detection using YOLOv8 face model
- Gaussian blur applied to detected face regions
- Live video feed display with blurred faces
- Press `r` to start/stop recording the processed video
- Press `q` to quit the application
- Output video saved as `output_clip.mp4`

---

##  Folder Structure

```

face-blur/
├── face-blur-live.py        # Main Python script
├── yolov8n-face.pt          # YOLOv8 face detection model (download separately)
├── output_clip.mp4          # (optional) Output video recorded on demand
└── README.md                # Project documentation

````

---

## ⚙️ Requirements

- Python 3.8 or higher
- Conda (recommended) or pip
- Packages:
  - `ultralytics`
  - `opencv-python`

---

## 🧪 Setup Instructions

### 1. Clone the Project
```bash
git clone https://github.com/yourusername/face-blur.git
cd face-blur
````

### 2. Create and Activate Environment

```bash
conda create -n face-blur python=3.8 -y
conda activate face-blur
```

### 3. Install Dependencies

```bash
pip install ultralytics opencv-python
```

### 4. Download YOLOv8 Face Detection Model

Download `yolov8n-face.pt` from the official release and place it in the project folder:

🔗 [Download yolov8n-face.pt](https://github.com/lindevs/yolov8-face/releases/download/v0.0.0/yolov8n-face.pt)

---

## ▶ Running the Script

### With Webcam:

```bash
python face-blur-live.py
```

The script will open a live webcam feed and blur any detected faces.

### Controls:

* **`r`** – Start/stop recording the output video
* **`q`** – Quit the application

---

##  Output

When you press `r`, the script starts saving the processed video (with blurred faces) to:

```bash
output_clip.mp4
```

Once you stop recording or quit the script, the file will be finalized and saved in the project folder.

---

##  Use with CCTV or IP Camera

To use a CCTV/IP feed instead of a webcam, modify the video source:

```python
cap = cv2.VideoCapture("rtsp://<your-camera-stream-url>")
```

---

##  Use Cases

* Privacy enforcement in public spaces
* Obscuring identity for anonymized data collection
* Smart surveillance systems

---

##  Possible Improvements

* Add timestamp or "REC" overlay during recording
* Save multiple clips with dynamic filenames
* Face pixelation instead of blur (for performance)
* Switch to other detection models (e.g., Haar cascades for lightweight use)


