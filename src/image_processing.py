import numpy as np
import random
import ctypes
import platform
import cv2

## Helper Functions
#make Dpi Aware - Fix
def fix_dpi():
    if int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)

#Helper Method to show image
def show_image(window,filename,image):
    cv2.imwrite(filename,image)
    window["-TOUT-"].update(filename)   
    window["-IMAGE-"].update(filename = filename)

#Image Processing
def generic_fft(filename):
    img = cv2.imread(filename)
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

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
    #return sp image
    return image

def noisy_fft():
    img = cv2.imread('noisy.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

#Method to Use a Median Blur on an image
def median_filter(filename):
    #Apply the Median Filter - 7X7 Kernel
    blurred_image = cv2.imread('noisy.png')
    blurred_image = cv2.blur(blurred_image,(7,7))
    #return image
    return blurred_image 

def blurred_fft():
    img = cv2.imread('blurred.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

#Method to Use a Gaussian Blur on an image
def gaussian_filter(filename):
    #Apply the Gaussian Filter - 7X7 Kernel
    gauss_image = cv2.imread('noisy.png')
    gauss_image = cv2.GaussianBlur(gauss_image,(7,7),0)
    #return image
    return gauss_image 

def gauss_fft():
    img = cv2.imread('gaussian.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

def edge_detection(filename):
    #Read in Image
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #Apply the Canny Edge Detection
    edges = cv2.Canny(image,100,150)
    #return image
    return edges

def edge_fft():
    img = cv2.imread('edges.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

#Color Space Modificationd
#Grayscale
def grayscale(filename):
    #Read in Image
    image = cv2.imread(filename)
    #Convert to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #return image
    return gray

def gray_fft():
    img = cv2.imread('gray.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

#HSV
def to_hsv(filename):
    #Read in Image
    image = cv2.imread(filename)
    #Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #return image
    return hsv

def hsv_fft():
    img = cv2.imread('hsv.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

#LUV
def to_luv(filename):
    #Read in Image
    image = cv2.imread(filename)
    #Convert to HSV
    luv = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
    #return image
    return luv

def luv_fft():
    img = cv2.imread('luv.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

#LAB
def to_lab(filename):
    #Read in Image
    image = cv2.imread(filename)
    #Convert to LAB
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    #return image
    return lab

def lab_fft():
    img = cv2.imread('lab.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

#RGB
def to_rgb(filename):
    #Read in Image
    image = cv2.imread(filename)
    #Convert to RGB
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #return image
    return rgb

def rgb_fft():
    img = cv2.imread('rgb.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag

#XYZ
def to_xyz(filename):
    #Read in Image
    image = cv2.imread(filename)
    #Convert to RGB
    xyz = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
    #return image
    return xyz

def xyz_fft():
    img = cv2.imread('xyz.png')
    #take fft of the image
    freq = np.fft.fft2(img)
    #shift so that DC component is in the center of the image
    corrected = np.abs(np.fft.fftshift(freq))
    #show magnitude spec. in dB
    mag = 20*np.log(corrected)
    #return freq spectrum
    return mag
