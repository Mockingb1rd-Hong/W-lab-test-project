import cv2

# Save video part as another file
vid_path = "/Users/yonghong/labtestproj/tsuzuku.mp4"
video = cv2.VideoCapture(vid_path)

parts = [(450, 1100)]
origin_video = cv2.VideoCapture(vid_path)
ret, frame = origin_video.read()
h, w, _ = frame.shape

fourcc = cv2.VideoWriter_fourcc(*"XVID")
writers = [cv2.VideoWriter(f"part{start}-{end}.mp4v", fourcc, 20.0, (w, h)) for start, end in parts]

f = 0
while ret:
    f += 1
    for i, part in enumerate(parts):
        start, end = part
        if start <= f <= end:
            writers[i].write(frame)
    ret, frame = origin_video.read()

for writer in writers:
    writer.release()

origin_video.release()
