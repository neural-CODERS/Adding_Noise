import cv2
import numpy as np 

img = cv2.imread("F:\\Downloads\\histogram2.png",cv2.IMREAD_COLOR)

gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
noise = img + img * gauss
cv2.imshow('Noise img',noise)
cv2.waitKey(0)
