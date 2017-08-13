# -*- coding: utf-8 -*-
import cv2
import numpy as np

# cv2.cv.CV_FOURCC
def cv_fourcc(c1, c2, c3, c4):
    return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
        ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)


if __name__ == '__main__':
    # 定数定義
    ESC_KEY = 27     # Escキー
    INTERVAL= 33     # 待ち時間
    FRAME_RATE = 30  # fps

    ORG_WINDOW_NAME = "org"
    BLUE_WINDOW_NAME = "blue"
    GREEN_WINDOW_NAME = "green"
    RED_WINDOW_NAME = "red"

    DEVICE_ID = 0

    # カメラ映像取得
    cap = cv2.VideoCapture(DEVICE_ID)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,320) 
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,240) 
    end_flag, c_frame = cap.read()

    # ウィンドウの準備
    cv2.namedWindow(ORG_WINDOW_NAME)
    cv2.namedWindow(BLUE_WINDOW_NAME)
    cv2.namedWindow(GREEN_WINDOW_NAME)
    cv2.namedWindow(RED_WINDOW_NAME)
    
    height, width, channels = c_frame.shape
    zero_img = np.zeros((height, width), dtype=np.uint8)

    # 変換処理ループ
    while end_flag == True:
	b,g,r = cv2.split(c_frame)
	b_frame = cv2.merge((b, zero_img, zero_img))
	g_frame = cv2.merge((zero_img, g, zero_img))
	r_frame = cv2.merge((zero_img, zero_img, r))

        # フレーム表示
        cv2.imshow(ORG_WINDOW_NAME, c_frame)
        cv2.imshow(BLUE_WINDOW_NAME, b_frame)
        cv2.imshow(GREEN_WINDOW_NAME, g_frame)
        cv2.imshow(RED_WINDOW_NAME, r_frame)


        # Escキーで終了
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        # 次のフレーム読み込み
        end_flag, c_frame = cap.read()

    # 終了処理
    cv2.destroyAllWindows()
    cap.release()
