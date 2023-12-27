import cv2
import cvzone
import pickle
import numpy as np


def checkSpace(imgprepop,img,positionList):
    available =0
    unavailable =0
    available_list=[]
    for ele,pos in enumerate(positionList):
        x1,y1 = pos[0],pos[1]
        x2,y2 = pos[2],pos[3]
        imgCrop = imgprepop[y1:y2,x1:x2]
        count = cv2.countNonZero(imgCrop)
        if y2-y1==22 and count<70:
            available+=1
            available_list.append(ele)
            cv2.rectangle(img, (x1,y1), (x2,y2), (0, 255, 0), 2)
        elif y2-y1 == 32 and count<78:
            available += 1
            available_list.append(ele)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        else:
            unavailable += 1
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        dis = 0
        cvzone.putTextRect(img, "available spaces:", (20, 710), 0.8, 1, (255, 0, 255), 0)
        for i in available_list:
            cvzone.putTextRect(img, "ParkID " + str(i), (145 + dis, 710), 0.8, 1, (255, 0, 255), 0)
            dis = dis + 75



def camera3_Clicked(source_vid,source_details):
    cap = cv2.VideoCapture(source_vid)

    with open(source_details, 'rb') as f:
        positionList = pickle.load(f)


    while (cap.isOpened()):
        success,img = cap.read()
        imgGray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
        imgMedian = cv2.medianBlur(imgThreshold,5)
        kernel = np.ones((3,3),np.uint8)
        imgDialate = cv2.dilate(imgMedian,kernel,iterations=1)

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)

        checkSpace(imgDialate,img,positionList)

        cv2.imshow("Image",img)
        if cv2.waitKey(10) & 0XFF == ord('q'):
            break

