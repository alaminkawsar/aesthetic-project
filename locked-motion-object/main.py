import cv2
import numpy as np
import pandas as pd
from process_image import process_image


def main(csv_path: str, img_folder_path: str, annotated_dir_path: str):
    
    """Load bounding boxes from a CSV file"""
    df = pd.read_csv(csv_path)
    bounding_boxes = df.values
    
    # Load image according to created time
    for i in range(1, len(bounding_boxes)):
        image_path = img_folder_path + "/frame" + str(i) + ".jpg"
        box = bounding_boxes[i]
        x1, y1, x2, y2 = map(int, box)  # Convert to integers
        box = [x1, y1, x2, y2]
        # print("box: ", box)
        
        save_processed_image_path = annotated_dir_path + "/frame_annotated_" + str(i) + ".png"
        process_image(img_path=image_path, box=box, save_processed_image_path=save_processed_image_path)
        print("Processed image: ", i)
        
    print("All images processed!")
    print(f"annotated image saved in {annotated_dir_path}!")

if __name__ == "__main__":
    csv_path = "data/bboxes.csv"
    img_folder = "data/frames2_raw_video"
    annotated_dir = "data/annotated_frame"
    main(csv_path=csv_path, img_folder_path=img_folder, annotated_dir_path=annotated_dir)