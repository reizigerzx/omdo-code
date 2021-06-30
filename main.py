import mediapipe_utils as mputil
import excel_utils as xlutil

video_path = ""

if __name__ == '__main__':
    mputil.use_logger(True)
    mputil.load_from_webcam()

