import os
import pickle
import face_recognition

DATASET_DIR = "dataset"
DATA_DIR = "data"
ENCODINGS_PATH = os.path.join(DATA_DIR, "face_encodings.pkl")

os.makedirs(DATA_DIR, exist_ok=True)

def build_encodings(model="hog"):
    known_encodings = []
    known_names = []

    if not os.path.isdir(DATASET_DIR):
        raise RuntimeError("dataset/ folder not found")

    for person_name in sorted(os.listdir(DATASET_DIR)):
        person_dir = os.path.join(DATASET_DIR, person_name)
        if not os.path.isdir(person_dir):
            continue

        print(f"Processing {person_name}...")
        for img_name in sorted(os.listdir(person_dir)):
            if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
                continue

            img_path = os.path.join(person_dir, img_name)

            image = face_recognition.load_image_file(img_path)
            face_locations = face_recognition.face_locations(image, model=model)
            if len(face_locations) == 0:
                print(f"  [WARN] No face in {img_path}")
                continue

            encodings = face_recognition.face_encodings(image, face_locations)
            for enc in encodings:
                known_encodings.append(enc)
                known_names.append(person_name)

    if not known_encodings:
        raise RuntimeError("No encodings generated. Check dataset images.")

    data = {"encodings": known_encodings, "names": known_names}
    with open(ENCODINGS_PATH, "wb") as f:
        pickle.dump(data, f)

    print(f"[INFO] Saved {len(known_encodings)} encodings "
          f"for {len(set(known_names))} people.")

if __name__ == "__main__":
    build_encodings(model="hog")   # use "cnn" only if you know dlib is compiled with CUDA
