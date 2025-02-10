from ultralytics import SAM
from PIL import Image
import cv2
import numpy as np
from ultralytics.models.sam import SAM2VideoPredictor

# Load a model
model = SAM("sam2.1_b.pt")  
model.info()

# Create SAM2VideoPredictor
overrides = dict(conf=0.25, task="segment", mode="predict", imgsz=1024, model="sam2_b.pt")
predictor = SAM2VideoPredictor(overrides=overrides)


def annotation(res, save_path):
  box = res[0].boxes.xyxy.squeeze().tolist()
  # Get the annotated image (numpy array)
  annotated_image = res[0].plot()

  # Convert to PIL format for displaying
  annotated_pil = Image.fromarray(annotated_image)

  # Save the annotated image
  annotated_pil.save(save_path)

  # Display the annotated image
  annotated_pil.show()
  return box


# Run inference with single point
results = predictor(source="actual_video.mp4", points=[385, 250],stream=True)

frames_bbox = []
for idx, r in enumerate(results):
  save_path = f"annotated_{idx}.png"
  box = annotation(r, save_path)
  frames_bbox.append(box)
  print(f"process frame: {idx}")
  print(box)