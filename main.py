# photo analysis, video analysis
import random

import cv2

if __name__ == '__main__':
    # -1, cv2.IMREAD_COLOR :load an color image
    # 0, cv2.IMREAD_GRAYSCALE: load image in grayscale mode
    # 1, cv2.IMREAD_UNCHANGED: load image colored without transparency
    image = cv2.imread("Picture/Q4 2.PNG", -1)  # load in BGR

    # print(image.shape)  #prints arry of color code
    # image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)  #resizing image to 50%
    # image = cv2.resize(image, (600,400))       # changing size manually
    # image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    # image = cv2.imwrite("image var.jpg", image)  # this command will create a new picture

    # copy image and paste it somewhere else
    # tag = image[100:200, 400:800]
    # image[200:300, 600:1000] = tag

    cv2.imshow('Image', image)  # Image is printed
    # wait an infinite amount of time for us to press any key. if instead of 0,
    # i write 5, then it means 5 seconds
    # as soon as i click anything, then destroy everything
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""
    https://www.youtube.com/watch?v=wlYPhdTbRmk&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn&index=2
    for i in range(10):
        for j in range(image.shape[1]):
            image[i][j] = [0, 0, 0]   # random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
"""

