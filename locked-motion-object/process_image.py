# draw point on image
import cv2
import numpy as np

def process_image(img_path, box, save_processed_image_path):
    img = cv2.imread(img_path, cv2.COLOR_BGR2RGB)
    print(img_path)
    # image height, width, channel
    h, w, c = img.shape
    # print("Original image size: ", h, w, c)
    # find center point
    point = (int((box[0] + box[2]) / 2), int((box[1] + box[3]) / 2))
    radius = 2
    color = (0, 0, 255)
    thickness = 1
    cv2.circle(img, point, radius, color, thickness)
    # cv2.imwrite("temp/output.png", img)


    # draw box, circle 
    point1 = box[0], box[1]
    point2 = box[2], box[3]
    box_widht = point2[0] - point1[0]
    box_height = point2[1] - point1[1]
    
    color = (0, 255, 0)
    thickness = 2
    cv2.rectangle(img, point1, point2, color, thickness)


    # draw line
    # cv2.line(img, (0, point[1]), (point1[0], point[1]), (255, 0, 0), 2)
    # cv2.line(img, (point2[0], point[1]), (w, point[1]), (255, 0, 0), 2)
    # cv2.line(img, (point[0], 0), (point[0], point1[1]), (255, 0, 0), 2)
    # cv2.line(img, (point[0], point2[1]), (point[0], h), (255, 0, 0), 2)
    diff = [point1[0], point1[1], w - point2[0], h - point2[1]]
    # print("diff: ", diff)
    min_length = min(diff)
    # print("min_length: ", min_length)
    scalling = w / h
    # print("scalling: ", scalling)
    new_frame_height = min_length*2 + box_height
    new_frame_widht = new_frame_height * scalling
    temp_frame_widht = new_frame_widht - box_widht
    img = img[point1[1] - min_length : point2[1] + min_length, int(point1[0] - temp_frame_widht/2) : int(point2[0] + temp_frame_widht/2)]
    # print("cropped image size: ", img.shape)
    try:
        # resize image previous size
        resized_cropped = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
        # print("after resized image size: ", resized_cropped.shape)

        # cv2.imwrite("temp/output2.png", img)
        cv2.imwrite(save_processed_image_path, resized_cropped)
    except Exception as e:
        print("Error: ", e)
        
if __name__ == "__main__":
    img_path = "data/frames2_raw_video/frame209.jpg"
    box = [337, 208, 414, 286]
    save_processed_image_path = "temp/output.png"
    process_image(img_path=img_path, box=box, save_processed_image_path=save_processed_image_path)



