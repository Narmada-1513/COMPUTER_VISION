import cv2
photo=cv2.imread(“image_1.jpg”)
photo1=cv2.imread(“image_2.jpg”)
photo.shape
photo1.shape
photo1=photo1[0:300,:]
import numpy as np
photo_photo1_horizontal=np.hstack((photo,photo1))
cv2.imshow(“Horizontal”,photo_photo1_horizontal)
cv2.waitKey()
cv2.destroyAllWindows()
photo_photo1_vertical=np.vstack((photo,photo1))
cv2.imshow(“vertical”,photo_photo1_vertical)
cv2.waitKey()
cv2.destroyAllWindows()

