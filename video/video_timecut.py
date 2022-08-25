import cv2
import time

start=time.time()
cap = cv2.VideoCapture("G:/observer_compute_intelligence/data/youtubedl/video/Paris Street View - June 18, 2020 21_07.mp4")

total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('视频总帧数：{} \t 视频帧速：{}\t 视频大小：{}，{}'.format(total, fps, h, w))

size = (int(w), int(h))  # 原视频的大小
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('D:/Desktop/1/Paris Street View - June 18, 2020 21_07_9.mp4', fourcc, fps, size)

frameToStart = int((60 * 47 + 27) * fps)  # 开始帧 = 开始时间*帧率
frametoStop = int((60 * 48 + 34) * fps)  # 结束帧 = 结束时间*帧率
cap.set(cv2.CAP_PROP_POS_FRAMES, frameToStart)  # 设置读取的位置,从第几帧开始读取视频

current_frame = frameToStart
while (1):
    success, frame = cap.read() 
    if success:
        current_frame += 1
        if (current_frame >= 0 and current_frame <= frametoStop):
            videoWriter.write(frame)
        else:
            break
    else:
        print('end')
        break
end=time.time()
print(end-start)

