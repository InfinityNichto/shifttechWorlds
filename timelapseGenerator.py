import os
import subprocess

input_directory = "images/"  # Replace with the path to your image directory
output_file = "shifttech.mp4"
image_extension = ".png"  # Replace with the extension of your image files

# Set the delay between frames in milliseconds (10 ms in this case)
frame_delay = 10

# Use FFmpeg to create the time-lapse video
command = (
    f"ffmpeg -framerate 1000/{frame_delay} -pattern_type glob -i '{input_directory}/*{image_extension}' "
    f"-vf 'scale=8400:2400' -c:v libx264 -pix_fmt yuv420p {output_file}"
)

# Execute the FFmpeg command
subprocess.call(command, shell=True)

print("Time-lapse video created: " + output_file)
