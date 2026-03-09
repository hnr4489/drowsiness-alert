import cv2
import dlib
import numpy as np
from scipy.spatial import distance
import requests
import pygame

# 1. Setup Alarm
pygame.mixer.init()
try:
    pygame.mixer.music.load("alarm.wav")
except:
    print("Sound file missing")

# Use a try-block for the predictor to catch path errors
try:
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
except Exception as e:
    print(f"ERROR: Could not load dlib models: {e}")

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

EYE_THRESHOLD = 0.30 # More sensitive
COUNTER = 0

cap = cv2.VideoCapture(0)

print("--- AI ENGINE STARTED (Numpy 1.26.4 Fix) ---")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        continue

    # FORCE FIX: Triple-layer conversion to prevent RuntimeError
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # dlib prefers RGB
    gray = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2GRAY)
    img_final = np.array(gray, dtype=np.uint8) # The "Magic" line

    try:
        faces = detector(img_final)

        for face in faces:
            shape = predictor(img_final, face)
            coords = np.array([(shape.part(i).x, shape.part(i).y) for i in range(68)])

            leftEye = coords[36:42]
            rightEye = coords[42:48]
            ear = (eye_aspect_ratio(leftEye) + eye_aspect_ratio(rightEye)) / 2.0

            if ear < EYE_THRESHOLD:
                COUNTER += 1
                if COUNTER >= 8: # Fast trigger (~0.5 seconds)
                    cv2.putText(frame, "DROWSY!", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play()
                    
                    try:
                        requests.post("http://127.0.0.1:5000/log", json={"status": "Drowsy"}, timeout=0.5)
                        print(">>> ALERT SENT!")
                    except:
                        pass
            else:
                COUNTER = 0
                pygame.mixer.music.stop()

    except RuntimeError as e:
        print(f"AI Error: {e}")
        continue

    cv2.imshow("Drowsiness Detector", frame)
    if cv2.waitKey(1) == 27: break

cap.release()
cv2.destroyAllWindows()