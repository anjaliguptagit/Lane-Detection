import cv2
img = cv2.imread('calibration1.jpg',1)
r,corners = cv2.findChessboardCorners(img,(9,5),None)
cv2.drawChessboardCorners(img,(9,5),corners,True)
cv2.imshow('test2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()