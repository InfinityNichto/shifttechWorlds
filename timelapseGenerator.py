# ChatGPT generated
import cv2
import os

# Directory containing your sorted images
image_folder = 'images/'

# Define the frame rate and output video file name
frame_rate = 60  # Adjust as needed
output_video = 'shifttech.avi'

# Calculate the delay per image in milliseconds
delay_per_image = 10

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'XVID'), frame_rate, (width, height), isColor=True)

for image in images:
    img = cv2.imread(os.path.join(image_folder, image))
    video.write(img)
    
    # Add a delay to control the frame rate
    cv2.waitKey(delay_per_image)

cv2.destroyAllWindows()
video.release()
