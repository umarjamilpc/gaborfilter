import cv2
import numpy as np
cap=cv2.VideoCapture("video2.mp4")
size=((int(cap.get(3))),(int(cap.get(4))))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('your_video_.avi', fourcc, 30.0, size)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        cv2.imshow("reading.. video",frame)
        out.write(frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print("press button to continue...")
cv2.waitKey()
helmet=cv2.VideoCapture("your_video_.avi")
while(helmet.isOpened()):
    ret, frame = helmet.read()
    if ret == True:
        cv2.imshow("recorded video show",frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
helmet.release()




cap.release()
