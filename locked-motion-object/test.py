import cv2
import numpy as np
import pandas as pd


csv_path = "data/bboxes.csv"
df = pd.read_csv(csv_path)
bounding_boxes = df.values

# Example Usage
img_path = "data/frames2_raw_video/frame74.jpg"
box = bounding_boxes[73]
x1, y1, x2, y2 = map(int, box)  # Convert to integers
box = [x1, y1, x2, y2]
print(box)

img = cv2.imread(img_path, cv2.COLOR_BGR2RGB)
x1, y1, x2, y2 = box
color = (0, 255, 0)
thickness = 2
cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

# Show image
cv2.imshow("Image with Bounding Box", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
