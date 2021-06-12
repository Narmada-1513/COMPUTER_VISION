import cv2
import numpy as np

photo = cv2.imread(‘elena_2.jpg’)
cv2.imshow(“ELENA_1”, photo)
cv2.waitKey()
cv2.destroyAllWindows()

ap1 = 150
aq1 = 100
ap2 = 500
aq2 = 400
Elena_1 = photo[aq1:aq2, ap1:ap2]
cv2.imshow(“ELENA_1”, Elena_1)
cv2.waitKey()
cv2.destroyAllWindows()

photo1 = cv2.imread(‘elena_1.jpg’)
cv2.imshow(“ELENA_1”, photo1)
cv2.waitKey()
cv2.destroyAllWindows()

bp1 = 150
bq1 = 100
bp2 = 500
bq2 = 400
Elena_2 = photo1[bq1:bq2, bp1:bp2]
cv2.imshow(“ELENA_2”, Elena_2)
cv2.waitKey()
cv2.destroyAllWindows()

photo1 = cv2.imread(‘elena_1.jpg’)
photo1[aq1:aq2, ap1:ap2] = Elena_1
cv2.imshow(“Damon”, photo1)
cv2.waitKey()
cv2.destroyAllWindows()

photo = cv2.imread(‘elena_2.jpg’)
photo[aq1:aq2, ap1:ap2] = Elena_2
cv2.imshow(“Damon”, photo)
cv2.waitKey()
cv2.destroyAllWindows()
