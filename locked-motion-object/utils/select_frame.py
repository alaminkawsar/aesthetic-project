import os
import shutil

def move_frames(input_folder, output_folder):
    """
    Select specific frames from a folder of images.
    
    Parameters:
        input_folder (str): Folder containing images.
        output_folder (str): Folder where selected frames will be saved.
        frame_indices (list): List of frame indices to select.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i in range(330):
        input_file = os.path.join(input_folder, f"frame_{i}.jpg")
        output_file = os.path.join(output_folder, f"frame_{i}.jpg")
        if not os.path.exists(input_file):
            print(f"File not found: {input_file}")
            continue
        shutil.move(input_file, output_file)
        print(f"Saved: {output_file}")

input_folder = "data/frames2"
output_folder = "data/selected_frames"
move_frames(input_folder, output_folder)