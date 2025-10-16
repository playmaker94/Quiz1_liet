import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# Load the YOLOv8 face detection model
model = YOLO("yolov8n.pt")  # Ensure this file is in the same folder

# Open webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

# Initialize video writer (for recording)
out = None
recording = False
frame_count = 0  # For saving frames

print("📸 Press 'r' to start/stop recording, 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("❌ Failed to read frame from webcam.")
        break

    # Convert frame to RGB for YOLO
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    result = model.predict(source=frame_rgb, conf=0.5, verbose=False)[0]
    boxes = result.boxes.xyxy.cpu().numpy().astype(int)

    # Apply blur to each face detected
    for box in boxes:
        x1, y1, x2, y2 = box
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(frame.shape[1], x2), min(frame.shape[0], y2)

        # Extract and blur face region
        face_region = frame[y1:y2, x1:x2]
        blurred = cv2.GaussianBlur(face_region, (99, 99), 30)
        frame[y1:y2, x1:x2] = blurred

    # Save frame for review (optional)
    frame_count += 1
    if frame_count % 30 == 0:  # Save every 30th frame
        cv2.imwrite(f"saved_frame_{frame_count}.jpg", frame)

    # Display frame using matplotlib (headless-friendly)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title("🕵️ Face Blurring Feed")
    plt.axis('off')
    plt.pause(0.001)
    plt.clf()

    # Handle key input (headless workaround: use fixed duration or external trigger)
    # You can simulate key input or use a timer-based exit
    # For now, we'll run for 300 frames then exit
    if frame_count >= 300:
        print("👋 Auto exit after 300 frames.")
        break

    # If recording, save the frame
    if recording and out is not None:
        out.write(frame)

# Clean up
cap.release()
if out:
    out.release()
plt.close()