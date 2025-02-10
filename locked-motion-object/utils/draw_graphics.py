import cv2
import pandas as pd

# Load bounding box CSV file
def load_bounding_boxes(csv_file):
    """Load bounding boxes from a CSV file"""
    df = pd.read_csv(csv_file)
    return df.values  # Convert DataFrame to NumPy array

# Function to draw bounding boxes
def draw_bounding_box(image_path, bbox, save_path, color=(0, 255, 0), thickness=2):
    """
    Draws a bounding box on an image.
    
    Parameters:
    - image_path: Path to the image
    - bbox: List or tuple (x1, y1, x2, y2)
    - color: Color of the bounding box (default: green)
    - thickness: Thickness of the bounding box lines
    """
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image not found or invalid path!")

    x1, y1, x2, y2 = map(int, bbox)  # Convert to integers
    cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

    # Show image
    cv2.imshow("Image with Bounding Box", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example Usage
csv_file = "data/bboxes.csv"  # Path to your CSV file
img_folder = "data/frames2_raw_video"
annotated_dir = "data/annotated_frame"
bounding_boxes = load_bounding_boxes(csv_file)

print(len(bounding_boxes))
# Assuming first row contains one bounding box
image_path = "data/frames2_raw_video/frame1.jpg"  # Replace with your image path
print(bounding_boxes[0])
draw_bounding_box(image_path, bounding_boxes[0], save_path = "data/annotated_frame/frame_1.png")
