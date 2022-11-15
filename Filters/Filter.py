# importing opencv CV2 module 
import cv2 

import numpy as np
from matplotlib import pyplot as plt

# You can change the kernel size as you want
image = cv2.imread('K:/Projects practice/Blurry-Image-Detection-and-Modification/images/hello.png')
avging = cv2.blur(image,(10,10))
cv2.imshow('Averaging',avging) 
cv2.waitKey(0) 
key=cv2.destroyAllWindows()

# sharpen

sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(image, -1, sharpen_kernel)
cv2.imshow('sharpen', sharpen)
cv2.waitKey()
cv2.destroyAllWindows()

#denosing
img = cv2.imread('K:/Projects practice/Blurry-Image-Detection-and-Modification/images/hello.png')
b,g,r = cv2.split(img)           # get b,g,r
rgb_img = cv2.merge([r,g,b])     # switch it to rgb
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

b,g,r = cv2.split(dst)           # get b,g,r
rgb_dst = cv2.merge([r,g,b])     # switch it to rgb

plt.subplot(211),plt.imshow(rgb_img)
plt.subplot(212),plt.imshow(rgb_dst)
plt.show()

img = cv2.imread('K:/Projects practice/Blurry-Image-Detection-and-Modification/images/hello.png') 

# Median blurring 
medBlur = cv2.medianBlur(img,5) 
cv2.imshow('Media Blurring', medBlur) 
cv2.waitKey(0) 

# Bilateral Filtering 
bilFilter = cv2.bilateralFilter(img,9,75,75) 
cv2.imshow('Bilateral Filtering', bilFilter) 
cv2.waitKey(0)  



img = cv2.imread('K:/Projects practice/Blurry-Image-Detection-and-Modification/images/hello.png') 
blur = cv2.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.show()
cv2.waitKey(0) 


def variance_of_laplacian():
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    image = cv2.imread('K:/Projects practice/Blurry-Image-Detection-and-Modification/images/hello.png') 
    
    gauBlur = cv2.Laplacian(gray, cv2.CV_64F).var()
    return cv2.imshow('Gaussian Blurring', gauBlur) 
    cv2.waitKey(0) 
    
