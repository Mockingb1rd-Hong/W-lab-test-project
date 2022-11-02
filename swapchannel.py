import cv2

image_path = "/Users/yonghong/labtestproj/torutsuzuku.jpeg"
image = cv2.imread(image_path)
b, g, r = cv2.split(image)
image_1 = cv2.merge([g, r, r])
image_2 = cv2.merge([r, g, g])
image_3 = cv2.merge([b, b, r])

cv2.imshow('1', image_1)
cv2.imshow('2', image_2)
cv2.imshow('3', image_3)

cv2.waitKey(0)
cv2.destroyAllWindows()
