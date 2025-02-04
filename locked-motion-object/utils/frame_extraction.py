import cv2
import os

def extract_frames(video_path, output_folder, skip_frame=1):
    """
    Extract frames from a video at a specific rate.
    
    Parameters:
        video_path (str): Path to the video file.
        output_folder (str): Folder where frames will be saved.
        frame_rate (int): Extract one frame every `frame_rate` seconds.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Get frames per second
    print(f"Video FPS: {fps}")
    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Break when the video ends

        if frame_count % skip_frame == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved: {frame_filename}")
            saved_count += 1

        frame_count += 1
        if (frame_count>=1250):
            break

    cap.release()
    print("Frame extraction complete!")

# Example usage
video_file = "example2.mp4"  # Replace with the actual video file path
output_dir = "data/frames2"
extract_frames(video_file, output_dir, skip_frame=1)  # Extract one frame per second
