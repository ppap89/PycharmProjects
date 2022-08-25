import os
import cv2
import time

cut_frame = 300  
save_path = "D:/Desktop/1/images/%s_%s.jpg"

for root, dirs, files in os.walk(r"G:/observer_compute_intelligence/data/youtubedl/video/adelaide/[4K] Brisbane CBD Adelaide Street Walking.mp4"): 
    for file in files:
        if ('.mp4' in file):
            path = os.path.join(root, file)
            video = cv2.VideoCapture(path)
            video_fps = int(video.get(cv2.CAP_PROP_FPS))
            print(video_fps)
            current_frame = 0
            while (True):
                ret, image = video.read()
                current_frame = current_frame + 1
                if ret is False:
                    video.release()
                    break
                if current_frame % cut_frame == 0:
                    cv2.imwrite(save_path + '/' + file[:-4] + '_' + str(current_frame) + '.jpg', image) 
                    # cv2.imencode('.jpg', image)[1].tofile(save_path + '/' + file[:-4] + str(current_frame) + '.jpg')
                    print('正在保存' + file + save_path + '/' + file[:-4] + str(current_frame))
                    # print('正在保存' + file + millis + '/' + file[:-4] + str(current_frame))