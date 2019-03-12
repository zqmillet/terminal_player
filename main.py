import cv2
import time

from decode import decode

video_capture = cv2.VideoCapture('./videos/plus1s.mp4')
frame_per_second = video_capture.get(cv2.CAP_PROP_FPS)

while True:
    now = time.time()
    success, image = video_capture.read()
    if not success:
        break

    print(decode(image))
    sleep_time = 1/frame_per_second - (time.time() - now)
    time.sleep(sleep_time)
