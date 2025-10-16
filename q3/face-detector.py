import cv2
from ultralytics import YOLO
import mediapipe as mp
import matplotlib.pyplot as plt

# Load YOLOv8 face detection model
model = YOLO("yolov8n-face.pt")  # Ensure this file is in your project folder

# Load image
image_path = "test_image.jpg"  # Change this to your image filename
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=5)

# Run YOLOv8 face detection
results = model(img_rgb)
for result in results:
    boxes = result.boxes.xyxy.cpu().numpy().astype(int)
    for box in boxes:
        x1, y1, x2, y2 = box
        face_roi = img_rgb[y1:y2, x1:x2]
        result_mp = face_mesh.process(face_roi)

        if result_mp.multi_face_landmarks:
            for face_landmarks in result_mp.multi_face_landmarks:
                h, w, _ = face_roi.shape

                # Define landmark indices
                NOSE_TIP = 1
                LEFT_EYE = [33, 133]
                RIGHT_EYE = [362, 263]

                # Helper functions to get landmark points
                def get_point(index):
                    lm = face_landmarks.landmark[index]
                    return int(lm.x * w) + x1, int(lm.y * h) + y1

                def get_avg_point(indices):
                    xs = [face_landmarks.landmark[i].x * w for i in indices]
                    ys = [face_landmarks.landmark[i].y * h for i in indices]
                    return int(sum(xs) / len(xs)) + x1, int(sum(ys) / len(ys)) + y1

                # Get key points
                nose = get_point(NOSE_TIP)
                left_eye = get_avg_point(LEFT_EYE)
                right_eye = get_avg_point(RIGHT_EYE)

                # Draw results
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
                cv2.circle(img, nose, 4, (0, 255, 0), -1)
                cv2.circle(img, left_eye, 4, (255, 0, 0), -1)
                cv2.circle(img, right_eye, 4, (0, 0, 255), -1)

# Display the result using matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Face Detection and Landmark Localization")
plt.axis('off')
plt.show()