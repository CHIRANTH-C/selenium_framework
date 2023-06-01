import pyautogui
import cv2
import numpy as np

def recording():
    # specify resolution
    resolution = (1920, 1080)

    # speicify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")

    # filename
    filename = "Reocording.avi"

    # specify frames per sec
    fps = 60.0

    # Create a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # craete a empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    # resize the window
    cv2.resizeWindow("Live", 480, 270)

    while True:
        # take screenshot using Pyautogui
        img = pyautogui.screenshot()

        # convert screenshot to a numpy array
        frame = np.array(img)

        # convert from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # write into output file
        out.write(frame)

        # display recording screen
        cv2.imshow('Live', frame)

        # stop the recording when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break


    # release the video writer
    out.release()

    # quit all windows
    cv2.destroyAllWindows()

recording()