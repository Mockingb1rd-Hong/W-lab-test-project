import cv2
import numpy as np

image_path = "/Users/yonghong/labtestproj/torugray.jpeg"
image = cv2.imread(image_path)

cv2.imshow('image', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
