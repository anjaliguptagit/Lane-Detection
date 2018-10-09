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
#undistorting video frames
k=True
vid=cv2.VideoCapture('project_video.mp4')
while (k):
    ret,frame = vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if (cv2.waitKey(1) & 0xFF )== ord('q'):
        k=False
    undistorted = cv2.undistort(gray,cameraMatrix,distCoeffs)
    cv2.imshow('und',undistorted)
    undistorted = cv2.cvtColor(undistorted,cv2.COLOR_GRAY2BGR)
    undistorted1 = cv2.cvtColor(undistorted,cv2.COLOR_BGR2HSV)
#using Sobel operator on undistorted image
    output_x=cv2.Sobel(undistorted1,cv2.CV_16S,1,0)
    output_y=cv2.Sobel(undistorted1,cv2.CV_16S,0,1)
    c=output_y+output_x
    d=numpy.uint8(numpy.absolute(c))
    undistorted2 = cv2.cvtColor(d,cv2.COLOR_HSV2BGR)
    cv2.imshow('out',undistorted2)
vid.release()
cv2.destroyAllWindows()