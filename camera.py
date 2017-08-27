# coding:utf-8

import cv2
import time


ESC_KEY = 27     # Escキー
INTERVAL= 33     # 待ち時間
DEVICE_ID = 0


cap = cv2.VideoCapture(DEVICE_ID)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240) 
end_flag, c_frame = cap.read()
cv2.namedWindow("camera")

while end_flag == True:
    cv2.imshow("camera", c_frame)
    key = cv2.waitKey(INTERVAL)
    if key == ESC_KEY:
        break
    end_flag, c_frame = cap.read()

cv2.destroyAllWindows()
cap.release()

