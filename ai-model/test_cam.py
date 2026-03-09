import cv2

print("Testing Camera 0...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ ERROR: Could not connect to camera.")
else:
    while True:
        ret, frame = cap.read()
        
        if not ret or frame is None:
            print("Camera connected, but sending blank video!")
            break

        cv2.imshow("PURE CAMERA TEST - Press ESC to close", frame)

        if cv2.waitKey(1) == 27: # Press ESC to quit
            break

cap.release()
cv2.destroyAllWindows()