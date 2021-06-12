import cv2
import numpy as np
photo=np.zeros((1000,1000,3))
photo[1:,:1000]=[255,0,0]
photo[200:,:1000]=[122,255,0]
photo[500:,:1000]=[100,200,255]
photo.shape
cv2.imshow(“blank_image”,photo)
cv2.waitKey()
cv2.destroyAllWindows() 

