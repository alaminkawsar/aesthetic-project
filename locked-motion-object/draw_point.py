# draw point on image
import cv2
import numpy as np

img_path = "data/frames2_raw_video/frame1.jpg"
img = cv2.imread(img_path)

# image height, width, channel
h, w, c = img.shape
print("image size: ", h, w, c)

point = (375, 250)
radius = 5
color = (0, 0, 255)
thickness = 1
cv2.circle(img, point, radius, color, thickness)
cv2.imwrite("temp/output.png", img)


# draw box, circle 
ball_size = 40
point1 = (point[0] - ball_size, point[1] - ball_size)
point2 = (point[0] + ball_size, point[1] + ball_size)
color = (0, 255, 0)
thickness = 2
cv2.rectangle(img, point1, point2, color, thickness)


# draw line
# cv2.line(img, (0, point[1]), (point1[0], point[1]), (255, 0, 0), 2)
cv2.line(img, (point2[0], point[1]), (w, point[1]), (255, 0, 0), 2)
cv2.line(img, (point[0], 0), (point[0], point1[1]), (255, 0, 0), 2)
# cv2.line(img, (point[0], point2[1]), (point[0], h), (255, 0, 0), 2)
diff = [point1[0], point1[1], w - point2[0], h - point2[1]]
# print("diff: ", diff)
min_length = min(diff)
print("min_length: ", min_length)
scalling = w / h
print("scalling: ", scalling)
img = img[point1[1]- min_length : point2[1] + min_length, int(point1[0] - min_length * scalling) : int(point2[0] + min_length * scalling)]
print("image size: ", img.shape)

# resize image previous size
img = cv2.resize(img, (w, h))

cv2.imwrite("temp/output2.png", img)


