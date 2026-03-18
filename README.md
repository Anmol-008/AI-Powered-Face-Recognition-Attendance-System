# AI-Powered Face Recognition Attendance System

An end-to-end **automated attendance system** that uses real-time face recognition to mark classroom attendance from a webcam feed.  
It replaces manual roll calls and paper registers with a fast, accurate, and auditable pipeline built using Python, OpenCV, and the `face_recognition` library.

---

## 🚀 Features

- Real-time face detection and recognition from a webcam stream.
- Deep-learning–based facial embeddings using the `face_recognition` library.
- Automatic attendance logging to a CSV file with **Name, Date, Time**.
- Guarantees **only one attendance entry per student per day**.
- Folder-based dataset: each student has their own image folder.
- Easy to update: add/remove students by changing the dataset and rerunning a single script.
- Optimized to run smoothly on CPU-only machines using frame downscaling and frame-skipping.

---

## 🧱 Tech Stack

- **Language:** Python  
- **Core Libraries:**
  - OpenCV (`cv2`) – webcam access and image processing
  - `face_recognition` – face detection and 128‑D facial embeddings
  - NumPy – numerical operations
  - CSV / Python standard library – attendance logging

---

## 📁 Project Structure

Example layout:

```text```
project-root/
  dataset/
    Anmol/
      img1.jpg
      img2.jpg
      ...
    Vipin/
      img1.jpg
      img2.jpg
      ...
  data/
    face_encodings.pkl            # auto-generated
  Attendance/
    attendance.csv                # auto-generated
  build_encodings.py
  attendance_face_recognition.py
  haarcascade_frontalface_default.xml   # optional if you use it anywhere
  README.md
  .gitignore
You can keep dataset/, data/, and Attendance/ local (ignored by git) to avoid uploading personal face images and generated files.

📸 Preparing the Dataset
Create a dataset/ folder in the project root.

For each student/person, create a subfolder named exactly as you want the label to appear, for example:

text
dataset/
  Anmol/
    1.jpg
    2.jpg
    ...
  Vipin/
    1.jpg
    2.jpg
    ...
Add multiple clear face photos per person:

Front-facing, reasonably good lighting.

Slightly different angles and expressions for better robustness.

Prefer images where only that person’s face is clearly visible.

These images are used to generate the facial embeddings.

🧪 Installation
It’s recommended to use a virtual environment, but it’s not mandatory.

bash
pip install face-recognition opencv-python numpy
Make sure face_recognition (and its dependency dlib) installs correctly on your system.

🏗️ Step 1 – Build Face Encodings
Run the encoding script to scan the dataset and generate facial embeddings:

bash
python build_encodings.py
This script:

Walks through all subfolders of dataset/.

For each image, detects faces and computes a 128‑D embedding.

Stores embeddings and their corresponding names into data/face_encodings.pkl.

Important: Run this script again whenever you add/remove students or change photos.

🎥 Step 2 – Run the Attendance System
Start the real-time face recognition and attendance logging:

bash
python attendance_face_recognition.py
This script:

Opens the default webcam and reads frames continuously.

Downscales each frame and converts it to RGB for faster processing.

Detects faces and computes embeddings for each face in the frame.

Compares each embedding with stored encodings and finds the closest match using a distance metric.

Applies a distance threshold (e.g., 0.5) to decide whether to accept the match or label the face as "Unknown".

If a recognized name has not been marked yet for the current date, appends a row to Attendance/attendance.csv in the format:

text
Name,Date,Time
Anmol,2026-03-18,09:30:15
Draws bounding boxes and labels (name + distance) on the live video feed.

Press q in the window to exit.

📊 Attendance Output
All attendance data is stored in:

text
Attendance/attendance.csv
Columns:

Name – recognized label (student name).

Date – YYYY-MM-DD.

Time – HH:MM:SS.

Each student gets at most one row per day, which keeps the file clean and ready for:

Reports and dashboards

Monthly/semester-wise analysis

Integration with academic or HR systems

⚙️ Configuration & Tuning
You can tune the behavior in attendance_face_recognition.py:

Match threshold

python
if best_dist < 0.5:
    name = known_names[best_idx]
Lower threshold (e.g. 0.4) → stricter, fewer false positives but more "Unknown".

Higher threshold (e.g. 0.6) → more matches but higher risk of incorrect labels.

Performance

Frame scaling factor (e.g. fx=0.25, fy=0.25) for speed.

Optionally process every other frame to reduce CPU load.

Adjust these depending on your hardware and accuracy requirements.

🔐 Git & Privacy
If this project is public on GitHub, it’s usually best not to upload real face images or generated data.

Example .gitignore:

text
dataset/
data/
Attendance/
*.pkl
*.csv
Explain in this README that users should supply their own images in dataset/<name>/ before running the scripts.

✅ Possible Extensions
Web dashboard (Streamlit / Flask) to view, filter, and search attendance.

Database integration (MySQL / PostgreSQL) instead of CSV.

Admin panel to add/edit students and upload images.

Support for multiple classrooms or cameras.

Email / notification integration for attendance summaries.

🧑‍💻 Author
Anmol Agarawal

B.Tech in Computer Science and Engineering – Government Engineering College, Bharatpur

B.S. in Data Science and Applications – IIT Madras

Feel free to fork the project, open issues, or suggest improvements!

text

To “download” it, just create a new file called `README.md` in VS Code, paste this content, save it, then commit and push.
