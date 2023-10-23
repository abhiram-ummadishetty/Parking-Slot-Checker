import cv2
import cvzone
import pickle
import numpy as np


width = 112
height = 48
cap = cv2.VideoCapture('carpark.mp4')

with open('carparkdet', 'rb') as f:
    positionList = pickle.load(f)

def checkSpace(imgprepop):
    available =0
    unavailable =0
    for pos in positionList:
        imgCrop = imgprepop[pos[1]:pos[1]+height,pos[0]:pos[0]+width]
        # cv2.imshow(str(pos[0]*pos[1]),imgCrop)
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count),(pos[0],pos[1]+height-10),1,1,(255,0,255),0)
        if count<920:
            available+=1
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 255, 0), 2)
        else:
            unavailable+=1
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 0, 255), 2)
        cvzone.putTextRect(img,"available:"+str(available),(20,20),1,1,(255,0,255),0)
        cvzone.putTextRect(img, "unavailable:" + str(unavailable), (20, 50), 1, 1, (255, 0, 255), 0)

while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.uint8)
    imgDialate = cv2.dilate(imgMedian,kernel,iterations=1)

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    # for pos in positionList:
    #     # cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    checkSpace(imgDialate)

    cv2.imshow("Image", img)
    # cv2.imshow("Img",imgDialate)
    if cv2.waitKey(10) & 0XFF == ord('q'):
        break
