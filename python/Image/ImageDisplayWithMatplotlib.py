import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("doge.jpeg")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.xticks([]), plt.yticks([])
plt.show()