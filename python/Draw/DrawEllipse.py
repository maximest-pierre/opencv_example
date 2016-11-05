import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a blue ellipse
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

cv2.imshow("Ellipse", img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()