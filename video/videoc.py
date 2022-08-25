import shutil
import os
import time
import cv2


path = 'G:/observer_compute_intelligence/data/youtubedl/video/amsterdam/videos/amsterdam2022_2.mp4'

cap = cv2.VideoCapture(path)
c = 1
timeRate = 2  # 截取视频帧的时间间隔

while (True):
    ret, frame = cap.read()
    FPS = cap.get(5)
    if ret:
        frameRate = int(FPS) * timeRate  # 因为cap.get(5)获取的帧数不是整数，所以需要取整一下（向下取整用int，四舍五入用round，向上取整需要用math模块的ceil()方法）
        if (c % frameRate == 0):
            # 显示截取的帧图片、保存截取帧到本地
            t = time.time()
            millis = int(round(time.time() * 1000))
            fra = str(c)
            print(fra) 
            name = path.split('/')[-1].split('.')[0]
            cv2.imwrite("G:/observer_compute_intelligence/data/youtubedl/amsterdam_images/images/%s_%s.jpg" % (name, fra) ,frame)
        c += 1
        cv2.waitKey(0)
    
    else:
        print("所有帧都已经保存完成")
        break


cap.release()
