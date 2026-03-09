# 🛡️ Real-Time Drowsiness Detection & Alert Dashboard

An AI-powered safety system that monitors driver/user fatigue using Computer Vision and sends real-time alerts to a MERN stack web dashboard.

## 🚀 How it Works
1. **AI Brain (Python):** Uses `OpenCV` and `Dlib` to track Eye Aspect Ratio (EAR). When eyes stay closed for too long, it triggers an alarm.
2. **Real-time Alert:** The Python script sends a `POST` request to the Node.js server immediately.
3. **Web Dashboard (MERN):** The React frontend fetches alerts instantly from the backend to show a red warning status.

## 🛠️ Tech Stack
- **AI:** Python, Dlib, OpenCV, NumPy
- **Backend:** Node.js, Express.js
- **Frontend:** React.js
- **Communication:** REST API
