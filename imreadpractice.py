import cv2

# Load a single image and display it (imread)
image_path = "/Users/yonghong/labtestproj/torutsuzuku.jpeg"
image_item = cv2.imread(image_path)
# print(type(image_item))
# print(image_item.shape)
cv2.imshow("ToRu-", image_item)
cv2.waitKey(0)

cv2.destoryAllWindows()
