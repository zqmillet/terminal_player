import cv2
import time

from decode import decode

def play(file_path):
    video_capture = cv2.VideoCapture(file_path)
    frame_per_second = video_capture.get(cv2.CAP_PROP_FPS)

    MOVE_UP = '\033[F'

    while True:
        now = time.time()
        success, image = video_capture.read()
        if not success:
            break

        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        image, height = decode(image)
        print(MOVE_UP * height + image)
        sleep_time = 1/frame_per_second - (time.time() - now)
        time.sleep(sleep_time)

def testcases():
    play('./videos/plus1s.mp4')

if __name__ == '__main__':
    testcases()
