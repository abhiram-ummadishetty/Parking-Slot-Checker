import cv2
import pickle


width = 112
height = 48

try:
    with open('carparkdet','rb') as f:
        positionList = pickle.load(f)
except:
    positionList = []

def mouseclick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN :
        positionList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(positionList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                positionList.pop(i)

    with open('carparkdet','wb') as f:
        pickle.dump(positionList,f)

while True:
    img = cv2.imread("carParkImg.png")

    for pos in positionList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    # cv2.rectangle(img,(startp[0],startp[1]),(endp[0],endp[1]),(255,0,255),3)
    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mouseclick)

    cv2.waitKey(1)





    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
