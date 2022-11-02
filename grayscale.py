import cv2
import numpy as np

# Converting to grayscale
image_path = "/Users/yonghong/labtestproj/torutsuzuku.jpeg"
target_path = "/Users/yonghong/labtestproj/torugray.jpeg"
image = cv2.imread(image_path)

result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(target_path, result)

# Adding noise
mean = 0
var = 10
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (result.shape[0], result.shape[1]))

noisy_result = result + gaussian
cv2.normalize(noisy_result, noisy_result, 0, 255, cv2.NORM_MINMAX, dtype=-1)
noisy_result = noisy_result.astype(np.uint8)

# Smoothing
smooth_result = cv2.GaussianBlur(noisy_result, (1, 1), 1)

cv2.imshow('result',  result)
cv2.imshow('noisy result', noisy_result)
cv2.imshow('smooth result', smooth_result)
cv2.waitKey(0)

cv2.destoryAllWindows()
