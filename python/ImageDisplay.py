import numpy as np
import cv2

# Load an image in grayscale
img = cv2.imread("doge.jpeg", 0)
cv2.imshow("image", img)
key = cv2.waitKey(0)

cv2.destroyAllWindows()