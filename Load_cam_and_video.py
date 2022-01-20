import numpy as np
import cv2

if __name__ == '__main__':
    # now we load
    cap = cv2.VideoCapture(0)  # we write 0 coz we have 1 cam
    # cap = cv2.VideoCapture('destination of the video')

    # we wrote true because we want the frame to show us until we press a key
    while True:
        ret, frame = cap.read()  # frame is image and ret is if the image is captured or not
        # like if the camera is working and the code cannot access it
        # so it return false

        # This is the width and height of the canvas and 3 and 4 are the code to get it
        width = int(cap.get(3))
        height = int(cap.get(4))

        # now we need a canvas to put our image
        image = np.zeros(frame.shape, np.uint8)
        smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        image[:height // 2, :width // 2] = smaller_frame
        image[height // 2:, :width // 2] = smaller_frame
        image[:height // 2, width // 2:] = smaller_frame
        image[height // 2:, width // 2:] = smaller_frame

        cv2.imshow('frame', image)
        cv2.imshow('image', image)

        if cv2.waitKey(1) == ord('q'):  # waitkey returns the value of the key so if we press d, break
            break

    cap.release()
    cv2.destroyAllWindows()
