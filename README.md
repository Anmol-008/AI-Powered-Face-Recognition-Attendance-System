# 🎯 AI-Powered Face Recognition Attendance System

🚀 A real-time, automated attendance system using deep learning--based
face recognition\
💡 Designed to replace manual roll calls with a fast, scalable, and
intelligent solution

------------------------------------------------------------------------

## 🔥 Why This Project Matters

Manual attendance systems are:

-   ⏱️ Time-consuming\
-   ❌ Error-prone\
-   📄 Hard to manage at scale

✅ This system solves all of that by:

-   Automating attendance in real-time\
-   Reducing human error\
-   Creating structured, analyzable data

------------------------------------------------------------------------

## 🚀 Key Features

-   ⚡ Real-time face detection & recognition (webcam-based)\
-   🧠 128-D facial embeddings using deep learning (face_recognition)\
-   📊 Automated attendance logging (Name, Date, Time)\
-   ✅ Ensures one entry per student per day\
-   🏷️ Handles Unknown faces detection\
-   💻 CPU-optimized (no GPU required)\
-   🔄 Scalable & easy dataset updates

------------------------------------------------------------------------

## 🧠 System Architecture

    Dataset Images → Face Encoding → Stored Embeddings (.pkl)
            ↓
     Webcam Feed → Face Detection → Embedding Extraction
            ↓
       Face Matching (Distance Threshold)
            ↓
     Attendance Logging → CSV File

------------------------------------------------------------------------

## 📊 Performance & Metrics

  Metric                 Value
  ---------------------- --------------
  Recognition Accuracy   \~90--95%
  Processing Speed       \~10--15 FPS
  Embedding Size         128-D
  Duplicate Prevention   1 entry/day
  Hardware Requirement   CPU-only

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Category           Tools
  ------------------ -------------------------
  Language           Python
  CV Library         OpenCV
  Face Recognition   face_recognition (dlib)
  Data Handling      NumPy, CSV
  Storage            Pickle (.pkl)

------------------------------------------------------------------------

## 📁 Project Structure

    Facial-recognition/
    ├── dataset/
    ├── data/
    ├── Attendance/
    ├── attendance_cam.py
    ├── build_embeddings.py
    ├── haarcascade_frontalface_default.xml
    ├── assets/
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

## ⚙️ Installation

    pip install face-recognition opencv-python numpy

------------------------------------------------------------------------

## 🏗️ Usage

### 1️⃣ Prepare Dataset

    dataset/
      Anmol/
        1.jpg
        2.jpg

### 2️⃣ Generate Embeddings

    python build_embeddings.py

### 3️⃣ Run System

    python attendance_cam.py

Press **q** to exit.

------------------------------------------------------------------------

## 📊 Output

    Attendance/attendance.csv

Example:

    Name,Date,Time
    Anmol,2026-03-18,09:30:15

------------------------------------------------------------------------

## ⚙️ Configuration

    if best_dist < 0.5:

------------------------------------------------------------------------

## 🔐 Privacy

    dataset/
    data/
    Attendance/
    *.pkl
    *.csv

------------------------------------------------------------------------

## 🚀 Applications

-   Schools & Colleges\
-   Corporate Offices\
-   Online Proctoring\
-   Secure Access Systems

------------------------------------------------------------------------

## 👨‍💻 Author

**Anmol Agrawal**

-   B.Tech CSE -- Government Engineering College, Bharatpur\
-   B.S. Data Science -- IIT Madras

------------------------------------------------------------------------

## ⭐ Support

⭐ Star the repo\
🍴 Fork it\
🛠️ Contribute
