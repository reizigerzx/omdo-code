from typing import NamedTuple

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

__log = False
__face = True
__body = True

fps = 0

def change_setting():
  return

def use_face(value:bool):
  global __face
  __face = value
  return

def use_logger(state:bool):
  global __log
  __log = state
  return

def load_from_video(filename: str):
  __mp_capture(cv2.VideoCapture(filename))
  return

def load_from_webcam(camera: int = 0):
  __mp_capture(cv2.VideoCapture(camera))
  return

def load_from_image():
  return

def convert_to_xls():
  return

def get_face_keypoints():

  return

def __mp_capture(capture:cv2.VideoCapture) -> [] :
  with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while capture.isOpened():
      success, image = capture.read()
      if not success:
        continue
      image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
      # pass by reference.
      image.flags.writeable = False
      results = holistic.process(image)
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      if __face:
        __process_captured_face(image, results)
      if __body:
        __process_captured_body(image, results)
      cv2.imshow('MediaPipe Holistic', image)
      if cv2.waitKey(5) & 0xFF == 27:
        break
  capture.release()
  return

def __process_captured_face(image, results:NamedTuple) -> list:
  face_keypoints = []
  mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
  if results.face_landmarks is not None:
    for data_point in results.face_landmarks.landmark:
      face_keypoints.append({
        'X': data_point.x,
        'Y': data_point.y,
        'Z': data_point.z,
        'Visibility': data_point.visibility,
      })
  return face_keypoints

def __process_captured_body(image, results:NamedTuple) -> list:
  mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
  mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
  mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)