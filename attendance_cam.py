import os
import cv2
import csv
import pickle
from datetime import datetime

import face_recognition
import numpy as np

DATA_DIR = "data"
ENCODINGS_PATH = os.path.join(DATA_DIR, "face_encodings.pkl")
ATT_DIR = "Attendance"
ATT_CSV = os.path.join(ATT_DIR, "attendance.csv")

os.makedirs(ATT_DIR, exist_ok=True)

def load_encodings():
    if not os.path.exists(ENCODINGS_PATH):
        print("Encodings not found. Run build_encodings.py first.")
        return None, None
    with open(ENCODINGS_PATH, "rb") as f:
        data = pickle.load(f)
    return data["encodings"], data["names"]

def ensure_attendance_file():
    if not os.path.exists(ATT_CSV):
        with open(ATT_CSV, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Date", "Time"])

def load_today_marked():
    ensure_attendance_file()
    today = datetime.now().strftime("%Y-%m-%d")
    marked = set()
    with open(ATT_CSV, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == today:
                marked.add(row["Name"])
    return marked

def append_attendance(name):
    ensure_attendance_file()
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    with open(ATT_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, date_str, time_str])

def main():
    known_encodings, known_names = load_encodings()
    if known_encodings is None:
        return

    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Webcam not accessible")
        return

    today_marked = load_today_marked()
    print("Already marked today:", today_marked)
    print("Press 'q' to quit.")

    process_every_other_frame = True  # speed boost

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # shrink frame to 1/4 for speed
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = []
        face_encodings = []

        if process_every_other_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        process_every_other_frame = not process_every_other_frame

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            if len(distances) == 0:
                continue

            best_idx = np.argmin(distances)
            best_dist = distances[best_idx]

            name = "Unknown"
            # 0.5 is a good starting threshold; lower for stricter matching [web:7][web:13]
            if best_dist < 0.5:
                name = known_names[best_idx]
                if name not in today_marked:
                    append_attendance(name)
                    today_marked.add(name)
                    print(f"Attendance marked for {name}, dist={best_dist:.3f}")

            # scale back up to original size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom),
                          (0, 255, 0), cv2.FILLED)
            label = name if name == "Unknown" else f"{name} ({best_dist:.2f})"
            cv2.putText(frame, label, (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 1)

        cv2.imshow("Face Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
