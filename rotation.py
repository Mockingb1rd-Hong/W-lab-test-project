import cv2
import numpy as np

image_path = "/Users/yonghong/labtestproj/torutsuzuku.jpeg"
image = cv2.imread(image_path)
angle = 45

image_center = tuple(np.array(image.shape[1::-1]) / 2)
rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)

cv2.imshow('result',  result)
cv2.waitKey(0)
cv2.destoryAllWindows()
