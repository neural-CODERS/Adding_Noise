import cv2
from skimage.util import random_noise
import numpy as np 

img = cv2.imread("F:\\Downloads\\histogram2.png",cv2.IMREAD_COLOR)
noise_img = random_noise(img,mode='gaussian',mean=0,var=0.008)
noise_img = np.array(object=255*noise_img,dtype='uint8')
cv2.imshow('Noise img',noise_img)
cv2.waitKey(0)