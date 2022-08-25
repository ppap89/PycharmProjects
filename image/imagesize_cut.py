import numpy as np
import glob as glob
import cv2
import os
from random import randint
from time import time, sleep
from os import getpid
from multiprocessing import Process

# Returns a list of all folders with participant numbers
# img_path = glob.glob("F:/test/*jpg")
# for path in img_path:
#     img  = cv2.imread(path)
#     cv2.imshow('img',img)
#     cv2.waitKey(1000)


def imagesize_cut(path1):
    print('启动进程，进程号[%d].'% getpid())
    def img_resize(image):
        height, width = image.shape[0], image.shape[1]
        # 设置新的图片分辨率框架
        width_new = 512
        height_new = 288
        # 判断图片的长宽比率
        if width / height >= width_new / height_new:
            img_new = cv2.resize(
                image, (width_new, int(height * width_new / width)))
        else:
            img_new = cv2.resize(
                image, (int(width * height_new / height), height_new))
        return img_new
    
    def get_file(root_path,all_files=[]):
    
        files = os.listdir(root_path)
        for file in files:
            if not os.path.isdir(root_path + '/' + file):   # not a dir
                all_files.append(root_path + '/' + file)
            else:  # is a dir
                get_file((root_path+'/'+file),all_files)
        return all_files


    # 循环处理列表中的所有图片
    file_path = get_file(path1)
    print('%s begin....'% (path1))   
    for f in  file_path:
        print(f.strip()[0:-4])
        path =  f.strip() 
        print(path)
        try:
            img = cv2.imread(path)
            time_to_download = randint(5, 10)
            # img1 = img_resize(img)
            # cv2.imshow('img', img)
            # shape[0] height,shape[1] width
            hei = img.shape[0] - 30
            wid = img.shape[1]
            roiImg = img[0:hei, 0:wid]
            # # cv2.imshow("[ROIImg]", roiImg)
            # path = "E:/image_/image/" + f.strip()[0:-4] + ".jpg"
            cv2.imwrite(path,roiImg)
       
        except:
            continue
    print('%s 完成,耗费了%d秒' % (path1,time_to_download))

def main():
    start = time()
    p1 = Process(target = imagesize_cut, args= ('E:/image_/image/',))
    p1.start()
    # p2 = Process(target = imagesize_cut, args = ('G:/observer_compute_intelligence/data/youtubedl/image/image_training_20220113/image07/',))
    # p2.start()
    p1.join()
    # p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

# imagesize_cut('')

if __name__ == '__main__':

    main()
