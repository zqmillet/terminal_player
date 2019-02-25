import cv2

video_capture = cv2.VideoCapture('./videos/plus1s.mp4')

while True:
    success, image = video_capture.read()
    if not success:
        break

    import pdb; pdb.set_trace()
