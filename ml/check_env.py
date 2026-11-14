
import sys
print("Python:", sys.version.split()[0])

import cv2
print("OpenCV:", cv2.__version__)

import mediapipe as mp
print("MediaPipe:", mp.__version__)

import numpy as np
print("NumPy:", np.__version__)

import sklearn
print("scikit-learn:", sklearn.__version__)

import tensorflow as tf
print("TensorFlow:", tf.__version__)

import fastapi
print("FastAPI:", fastapi.__version__)

import pyttsx3
print("pyttsx3: OK")

# MediaPipe Tasks API test
from mediapipe.tasks.python import vision
print("MediaPipe Tasks API: OK")

# Camera test
cap = cv2.VideoCapture(0)
ok, frame = cap.read()
print("Camera:", "OK" if ok else "FAILED")
cap.release()

print("\nEnvironment check completed!")
