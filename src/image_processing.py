import numpy as np
import random
import ctypes
import platform
import cv2

#make the app dpi aware
def fix_dpi():
    if int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)

#Helper Method to add salt-and noise to an image
def salt_and_pepper(image):
    row,col = image.shape
    #color pixels white
    number_of_pixels = random.randint(300, 10000) 
    for i in range(number_of_pixels): 
        y_coord=random.randint(0, row - 1) 
        x_coord=random.randint(0, col - 1)
        image[y_coord][x_coord] = 255
    #color pixels black
    number_of_pixels = random.randint(300, 30000) 
    for i in range(number_of_pixels): 
        y_coord=random.randint(0, row - 1) 
        x_coord=random.randint(0, col - 1)
        image[y_coord][x_coord] = 0
    #return image
    return image

#Method to Use a Median Blur on an image
def median_filter(filename):
    #Add Salt and Pepper Noise to Image
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('noisy.png',salt_and_pepper(image))
    #Apply the Median Filter - 5X5 Kernel
    blurred_image = cv2.imread('noisy.png')
    blurred_image = cv2.blur(blurred_image,(5,5))
    #return image
    return blurred_image 

#Method to Use a Gaussian Blur on an image
def gaussian_filter(filename):
    #Add Salt and Pepper Noise to Image
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('noisy.png',salt_and_pepper(image))
    #Apply the Median Filter - 5X5 Kernel
    gauss_image = cv2.imread('noisy.png')
    gauss_image = cv2.GaussianBlur(gauss_image,(5,5),0)
    #return image
    return gauss_image 

def edge_detection(filename):
    #Read in Image
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #Apply the Median Filter - 5X5 Kernel
    edges = cv2.Canny(image,100,150)
    #return image
    return edges
