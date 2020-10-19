import cv2
import numpy as np
cv2.waitKey()
cap=cv2.VideoCapture("mujtaba.avi")
green_difference=np.zeros((int(cap.get(4)),(int(cap.get(3))),3),dtype="uint8")
size=((int(cap.get(3))),(int(cap.get(4))))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('your_video_try_low_frame.avi', fourcc, 15.0, size)

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        cv2.imshow("reading video",frame)
        #img_rotate_90_clockwise = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        for i in range(500):
           for j in range(500):
                green_difference[i][j][0] = abs(frame[i][j][1] - ((frame[i][j][2] + frame[i][j][0]) / 2))
                green_difference[i][j][1] = abs(frame[i][j][1] - ((frame[i][j][2] + frame[i][j][0]) / 2))
                green_difference[i][j][2] = abs(frame[i][j][1] - ((frame[i][j][2] + frame[i][j][0]) / 2))

        out.write(green_difference)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print("press button to continue...")
cv2.waitKey()
helmet=cv2.VideoCapture("your_video_try_low_frame.avi")
while(helmet.isOpened()):
    ret,frame=helmet.read()
    if ret == True:
        cv2.imshow("run recorded video",frame)
        #out.write(frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()