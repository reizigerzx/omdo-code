#TODO git mv or make sure the renamed find don't duplicate

import mediapipe_utils as mputil
import excel_utils as xlutil

video_name = "jiheon.webm"
sheet_name = "keypoint_result.xlsx"

def test_webcam():
  mputil.draw_keypoint = True
  mputil.use_keypoint = True
  mputil.set_resolution(1280, 720)
  mputil.load_from_webcam()

def test_video():
  mputil.draw_keypoint = True
  mputil.convert_to_xls(sheet_name)
  mputil.load_from_video(video_name)

if __name__ == '__main__':
  test_webcam()


