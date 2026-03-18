# 🎯 AI-Powered Face Recognition Attendance System

> 🚀 A real-time, automated attendance system using deep learning–based face recognition  
> 💡 Designed to replace manual roll calls with a fast, scalable, and intelligent solution

---

## 📸 Demo

### 🎥 Live Face Recognition in Action
![Demo GIF](assets/demo.gif)

### 📊 Sample Attendance Output
![CSV Output](assets/output.png)

> 📌 *(Add screenshots/GIFs in an `assets/` folder for maximum impact)*

---

## 🔥 Why This Project Matters

Manual attendance systems are:
- ⏱️ Time-consuming
- ❌ Error-prone
- 📄 Hard to manage at scale

✅ This system solves all of that by:
- Automating attendance in **real-time**
- Reducing human error
- Creating **structured, analyzable data**

---

## 🚀 Key Features

- ⚡ Real-time face detection & recognition (webcam-based)
- 🧠 128-D facial embeddings using deep learning (`face_recognition`)
- 📊 Automated attendance logging (Name, Date, Time)
- ✅ Ensures **one entry per student per day**
- 🏷️ Handles **Unknown faces detection**
- 💻 CPU-optimized (no GPU required)
- 🔄 Scalable & easy dataset updates

---

## 🧠 System Architecture

```text```
Dataset Images → Face Encoding → Stored Embeddings (.pkl)
        ↓
 Webcam Feed → Face Detection → Embedding Extraction
        ↓
   Face Matching (Distance Threshold)
        ↓
 Attendance Logging → CSV File
📊 Performance & Metrics
Metric	Value
Recognition Accuracy	~90–95% (good lighting conditions)
Processing Speed	~10–15 FPS (CPU)
Embedding Size	128-D vector
Duplicate Prevention	✅ 1 entry per day
Hardware Requirement	CPU-only

📌 Performance may vary based on lighting, dataset quality, and hardware

🛠️ Tech Stack
Category	Tools
Language	Python
CV Library	OpenCV
Face Recognition	face_recognition (dlib)
Data Handling	NumPy, CSV
Storage	Pickle (.pkl)
📁 Project Structure
Facial-recognition/
│
├── dataset/                      # Input images (per person)
│   ├── Anmol/
│   ├── Vipin/
│
├── data/
│   └── face_encodings.pkl
│
├── Attendance/
│   └── attendance.csv
│
├── attendance_cam.py
├── build_embeddings.py
├── haarcascade_frontalface_default.xml
├── assets/                       # (Add demo GIFs/screenshots here)
├── README.md
└── .gitignore
⚙️ Installation
pip install face-recognition opencv-python numpy

⚠️ Ensure dlib installs correctly

🏗️ Step-by-Step Usage
1️⃣ Prepare Dataset
dataset/
  Anmol/
    1.jpg
    2.jpg

✔ Use 5–10 images per person
✔ Ensure clear lighting & face visibility

2️⃣ Generate Face Embeddings
python build_embeddings.py

✔ Converts images → 128-D embeddings
✔ Saves to data/face_encodings.pkl

3️⃣ Run Attendance System
python attendance_cam.py

✔ Starts webcam
✔ Detects & recognizes faces
✔ Logs attendance automatically

Press q to exit.

📊 Output
Attendance/attendance.csv

Example:

Name,Date,Time
Anmol,2026-03-18,09:30:15

✔ Clean format
✔ No duplicate entries
✔ Ready for analytics

⚙️ Key Configurations
🎯 Matching Threshold
if best_dist < 0.5:
Threshold	Effect
0.4	Strict
0.5	Balanced
0.6	Loose
⚡ Performance Optimization

Resize frames (fx=0.25)

Process alternate frames

Works on low-end machines

🔐 Privacy & Security
dataset/
data/
Attendance/
*.pkl
*.csv

✔ Keep sensitive data local
✔ Do not upload face images to GitHub

🚀 Real-World Applications

🏫 Schools & Colleges

🏢 Corporate Attendance Systems

🎓 Online Proctoring

🔐 Secure Access Systems

🔮 Future Enhancements

📊 Web Dashboard (Streamlit)

🗄️ Database integration (MySQL/PostgreSQL)

📱 Mobile camera support

🧠 DeepFace / FaceNet integration

☁️ Cloud deployment (AWS/GCP)

👨‍💻 Author

Anmol Agrawal

🎓 B.Tech CSE – Government Engineering College, Bharatpur

🎓 B.S. Data Science – IIT Madras

⭐ Show Your Support

If you like this project:

⭐ Star the repository

🍴 Fork it

🛠️ Contribute
