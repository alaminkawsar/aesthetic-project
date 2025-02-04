import cv2
import os

def get_creation_time(image_path):
    """Get the creation time of an image file."""
    return os.path.getmtime(image_path)

def images_to_video(image_folder, output_video, fps=30):
    # Get list of images in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
    
    # Sort images by creation time
    images = sorted(images, key=lambda x: get_creation_time(os.path.join(image_folder, x)))

    # Read the first image to get the size
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # Loop through all images and write them to the video
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    # Release the video writer
    video.release()
    print(f"Video saved as {output_video}")

# Example usage
image_folder = 'data/frames2_raw_video'  # Replace with the path to your image folder
output_video = 'temp/actual_video.mp4'  # Name of the output video file
fps = 23  # Frames per second

images_to_video(image_folder, output_video, fps)