import cv2
import numpy as np
cap = cv2.VideoCapture('video2.mp4')
green_difference=np.zeros((int(cap.get(4)),(int(cap.get(3))),3),dtype="uint8")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('umarvideo.mp4', fourcc, 20.0, size)

while(cap.isOpened()):
    ret , frame = cap.read()
    print(frame.shape[0])
    print(frame.shape[1])
    if ret == True:
        #cv2.imshow('Recording...', frame)

        # h=(frame.shape[0])//2
        # b=(frame.shape[1])//2
        # centre=(h,b)
        # m=cv2.getRotationMatrix2D(centre,135,1.0)
        # frame=cv2.warpAffine(frame,m,(b,h))
        # print(frame.shape[0])
        # print(frame.shape[1])
        #
        value=frame
        #cv2.imshow('Recording..', value)
        for i in range(700):
            for j in range(700):
                green_difference[i][j][0] = abs(value[i][j][1] - ((value[i][j][2] + value[i][j][0]) / 2))
                green_difference[i][j][1] = abs(value[i][j][1] - ((value[i][j][2] + value[i][j][0]) / 2))
                green_difference[i][j][2] = abs(value[i][j][1] - ((value[i][j][2] + value[i][j][0]) / 2))






        out.write(green_difference)
    else:
            break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print("finised program")
cap.release()
out.release()
cv2.destroyAllWindows()