import cv2
import face_recognition
import os
from utils import speak

# Load known faces
KNOWN_FACES_DIR = "faces"   # folder containing known people's images
TOLERANCE = 0.6
MODEL = "hog"   # "cnn" for GPU (slower but more accurate)

known_faces = []
known_names = []

def load_faces():
    """Load known faces from folder"""
    for name in os.listdir(KNOWN_FACES_DIR):
        person_dir = os.path.join(KNOWN_FACES_DIR, name)
        if not os.path.isdir(person_dir):
            continue

        for filename in os.listdir(person_dir):
            image = face_recognition.load_image_file(os.path.join(person_dir, filename))
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(name)
    speak("Facial recognition data loaded.")


def recognize_face():
    """Start webcam and recognize faces"""
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(rgb_frame, model=MODEL)
        encodings = face_recognition.face_encodings(rgb_frame, locations)

        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None

            if True in results:
                match = known_names[results.index(True)]
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, match, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                speak(f"Hello {match}, welcome back!")
            else:
                speak("Unknown person detected.")

        cv2.imshow("Chuck's Vision", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
