# -*- coding: utf-8 -*-
import cv2
import numpy as np

# cv2.cv.CV_FOURCC
def cv_fourcc(c1, c2, c3, c4):
    return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
        ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)

def filter_popart(org_img):
    b,g,r = cv2.split(org_img)
    b_rnd,g_rnd,r_rnd = np.random.randint(0,255,(3))
    return cv2.merge((b - b_rnd, g - g_rnd, r - r_rnd))

def filter_rgb_shuffle(org_img):
    bgr = cv2.split(org_img)
    np.random.shuffle(bgr)
    return cv2.merge((bgr[0], bgr[1], bgr[2]))

if __name__ == '__main__':
    # 定数定義
    ESC_KEY = 27     # Escキー
    INTERVAL= 33     # 待ち時間
    FRAME_RATE = 30  # fps

    ORG_WINDOW_NAME = "random"

    DEVICE_ID = 0

    # カメラ映像取得
    cap = cv2.VideoCapture(DEVICE_ID)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640) 
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480) 
    end_flag, c_frame = cap.read()

    # ウィンドウの準備
    cv2.namedWindow(ORG_WINDOW_NAME)
    
    height, width, channels = c_frame.shape
    zero_img = np.zeros((height, width), dtype=np.uint8)

    # 変換処理ループ
    while end_flag == True:
	#dest_frame = filter_popart(c_frame)
	#dest_frame = filter_rgb_shuffle(c_frame)
	dest_frame = filter_rgb_shuffle(filter_popart(c_frame))
        # フレーム表示
        cv2.imshow(ORG_WINDOW_NAME, dest_frame)


        # Escキーで終了
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        # 次のフレーム読み込み
        end_flag, c_frame = cap.read()

    # 終了処理
    cv2.destroyAllWindows()
    cap.release()
