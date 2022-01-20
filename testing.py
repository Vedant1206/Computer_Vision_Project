
import cv2

if __name__ == '__main__':
    image = cv2.imread('Picture/pic.JPG')
    cv2.imshow('spic', image)

    cv2.waitKey()
    cv2.destroyAllWindows()



