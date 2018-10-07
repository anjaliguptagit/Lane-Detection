import cv2
import numpy
import glob
img_list = glob.glob('*.jpg') #list of input images
objp = numpy.zeros((9*6,3),numpy.float32)
objp[:,:2] = numpy.mgrid[0:9,0:6].T.reshape(-1,2) #objectpoints of images
#reading image and identifying corners
imgpoints = []
objpoints = []
for image in img_list:
    img = cv2.imread(image,0)
    r,corners = cv2.findChessboardCorners(img,(9,6),None)
    imgpoints.append(corners)
    objpoints.append(objp)
#finding camera's intrinsic parameters	
r2,cameraMatrix,distCoeffs,rvecs,tvecs = cv2.calibrateCamera(objpoints,imgpoints,img.shape[::-1],None,None)
#for img in img_list:
#img=cv2.imread('calibration2.jpg',0)
#undistorted = cv2.undistort(img,cameraMatrix,distCoeffs)
import matplotlib.image as mpi
img = mpi.imread('calibration2.jpg')
undistorted = cv2.undistort(img,cameraMatrix,distCoeffs)
cv2.imshow('und',undistorted)
output_x=cv2.Sobel(undistorted,-1,1,0)
output_y=cv2.Sobel(undistorted,-1,0,1)
c=output_x+output_y
cv2.imshow('out',c)
cv2.waitKey(0)
cv2.destroyAllWindows
'''
#displaying the chessboard corners
cv2.drawChessboardCorners(img,(9,5),corners,r)
cv2.imshow('test2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#creating distortion matrix
    