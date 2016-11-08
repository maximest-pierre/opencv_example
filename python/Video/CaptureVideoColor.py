import numpy as np
import cv2

video = cv2.VideoCapture(0)

while (True):

    ret, frame = video.read()


    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
