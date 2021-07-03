from typing import NamedTuple
import numpy as np
import cv2
import mediapipe as mp

import excel_utils

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
width, height = [0,0]

processFace, processBody, processLeftHand, processRightHand  = [True, True, True, True]
face_keypoints,body_keypoints,left_hand_keypoints,right_hand_keypoints = [[],[],[],[]]

__is_video = False
draw_keypoint = True
use_keypoint = False
log_keypoint = False

captured_frame = 0
keypoint_captured_frame = 0

def set_resolution(_width:int, _height:int):
  global width, height
  width = _width
  height = _height

def load_from_video(filename: str):
  __mp_capture(cv2.VideoCapture(filename))
  return

def load_from_webcam(camera: int = 0 ):
  __mp_capture(cv2.VideoCapture(camera))
  return

def load_from_image():
  return

def convert_to_xls(filename:str):
  excel_utils.write_xlsx(keypoint_captured_frame,face_keypoints, filename)
  return

def show_fps():
  return

def __mp_capture(_capture:cv2.VideoCapture) -> [] :

  def process_keypoint(_image:np.ndarray, _results, _keypoint_type):
    if draw_keypoint: mp_drawing.draw_landmarks(_image, _results, _keypoint_type)
    keypoints = []
    if _results is not None and use_keypoint:
      for data_point in _results.landmark:
        keypoints.append({ 'X': data_point.x, 'Y': data_point.y,'Z': data_point.z, 'Visibility': data_point.visibility,})
      if log_keypoint: print(str(keypoints))
    return keypoints

  with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while _capture.isOpened():
      success, image = _capture.read()
      if not success:
        continue
      #_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
      #_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
      image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
      # pass by reference.
      image.flags.writeable = False
      results = holistic.process(image)
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      global face_keypoints,body_keypoints,left_hand_keypoints,right_hand_keypoints
      if processFace: face_keypoints = process_keypoint(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
      if processBody: body_keypoints = process_keypoint(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
      if processLeftHand : left_hand_keypoints = process_keypoint(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
      if processRightHand: right_hand_keypoints = process_keypoint(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
      cv2.imshow('MediaPipe Holistic', image)
      if cv2.waitKey(5) & 0xFF == 27:
        break
  _capture.release()
  return