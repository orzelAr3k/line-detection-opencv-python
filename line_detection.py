import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny(image):
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)   # Kernel size is 5x5
    canny = cv2.Canny(blur,50,150)
    return canny


def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(200,height),(1100,height),(550,250)]
    ])          # Triangle polygon because cv2.fillPoly expects an array of polygons.
    mask = np.zeros_like(image)   # Create a black mask to apply the above Triangle on.
    cv2.fillPoly(mask,polygons,255)     # A complete white triangle polygon on a black mask.
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image


if __name__ == "__main__":

    image = cv2.imread('images/test_image.jpg')
    lane_image = np.copy(image)     # Always make a copy when working with arrays rather than directly assigning
    canny_image = canny(lane_image)
    cropped_image = region_of_interest(canny_image)   
    cv2.imshow('Result', cropped_image) # Canny image with region of interest
    cv2.waitKey(0)

  