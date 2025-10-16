Absolutely! Here’s the complete combined README.md including setup, running instructions, dependencies, and assumptions — ready to drop into your project folder:

# Face Detection and Feature Localization using YOLOv8 and Mediapipe

This project detects faces in images using a YOLOv8 face detection model and localizes facial features such as the tip of the nose and centers of the eyes using Mediapipe FaceMesh. The detected faces and key points are then annotated and displayed.

---

## Requirements

- Python 3.8 or higher
- Conda (recommended) or pip environment

---

## Dependencies

The project requires the following Python packages:

- `ultralytics` (YOLOv8 framework)  
  For loading and running the YOLOv8 face detection model.
  
- `mediapipe`  
  For detecting detailed facial landmarks such as nose tip and eye centers.

- `opencv-python`  
  For image processing, visualization, and display.

### Installation:

Use pip to install dependencies:

```bash
pip install ultralytics mediapipe opencv-python


Or create a fresh conda environment and install:

conda create -n face-detection python=3.8 -y
conda activate face-detection
pip install ultralytics mediapipe opencv-python

Assumptions

The input images contain clear, front-facing human faces for accurate detection.

YOLOv8 face detection model (yolov8n-face.pt) is used, which is specialized for face detection, not the general YOLOv8 model.

Mediapipe FaceMesh provides 468 facial landmarks, and specific landmark indices are used to approximate the centers of the eyes.

The script runs in an environment capable of opening image display windows (GUI support).

The yolov8n-face.pt model file is downloaded and placed in the same directory as the Python script.

Python 3.8+ is used, as some dependencies may not support older versions.

Setup Instructions

Clone or download this repository and navigate to the project folder.

Create and activate the Conda environment (optional but recommended):

conda create -n face-detection python=3.8 -y
conda activate face-detection


Install required Python packages:

pip install ultralytics mediapipe opencv-python


Download the YOLOv8 face detection model:

Download yolov8n-face.pt from the link below and place it in the project folder:

yolov8n-face.pt Download Link

Add your test image(s) to the project folder:

Place the image file (e.g., face1.jpg) you want to test in the same folder as the script.

How to Run the Code

Open your terminal or command prompt.

Activate your Conda environment if not already activated:

conda activate face-detection


Run the face detection script:

python face-detector.py


The script will open a window displaying the input image with:

Yellow bounding boxes around detected faces

Green dot for the nose tip

Blue and red dots for the centers of the left and right eyes

Press any key while the window is focused to close the display window.

Notes

The script uses the Mediapipe FaceMesh model which detects 468 facial landmarks.

The eye centers are approximated by averaging two key landmarks for each eye.

The YOLOv8 model is downloaded separately to ensure precise face detection.

Troubleshooting

If you get errors related to missing packages, ensure you installed all requirements with pip.

If the image window does not appear, make sure you are running the script in an environment with GUI support.

Use images with clear, front-facing faces for best results.


