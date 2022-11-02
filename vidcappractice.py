import cv2

vid_path = "/Users/yonghong/labtestproj/tsuzuku.mp4"
video = cv2.VideoCapture(vid_path)

# Load Video
if not video.isOpened():
    print('File not accessible or not exist')

ret, frame = video.read()
if ret:
    cv2.imshow('Frame', frame)
    cv2.waitKey(20)

video.release()
cv2.destroyAllWindows()



