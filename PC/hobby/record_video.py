import cv2
import numpy as np
import pyautogui
import keyboard as kb


# display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# frames per second
fps = 12.0
# create the video write object
video_out = cv2.VideoWriter("d:\output.mp4", fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds
record_seconds = 10

# for i in range(int(record_seconds * fps)):
while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    video_out.write(frame)
    # show the frame
    # cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits- 
    if kb.is_pressed("q"):
        break
# make sure everything is closed when exited
cv2.destroyAllWindows()
video_out.release()
