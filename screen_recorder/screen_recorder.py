import numpy as np
import pyautogui
import cv2
import datetime as dt

print("Key Commands:")
print("s - Start")
print("w - Pause/Resume")
print("q - Quit")

# Create VideoWriter
resolution = (1920, 1080)
fps = 60
codec = cv2.VideoWriter_fourcc(*'XVID')
filename = dt.datetime.now().strftime('%m-%d-%Y_%H-%M_recording.avi')

recording = cv2.VideoWriter(filename, codec, fps, resolution)

# Create preview window
cv2.namedWindow('Preview', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Preview', 480, 270)

start = False
pause = False

while True:
    # Record when the process has started but if it's not paused
    if start and not pause:
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        recording.write(frame)
        cv2.imshow('Preview', frame)

    key = cv2.waitKey(1)  # Receive key commands
    if key == ord('q'):
        print("Recording ended.")
        break
    elif key == ord('s'):
        if not start:
            print("Recording started. Press 'q' to end recording.")
            start = True
    elif key == ord('w') and start:
        pause = not pause
        if pause:
            print("Recording paused. Press 'w' to resume recording.")
        else:
            print("Recording resumed.")

recording.release()
cv2.destroyAllWindows()
