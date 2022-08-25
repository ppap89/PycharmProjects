import cv2
import queue
import time
import threading
import os
q=queue.Queue()

def get_file(root_path,all_files=[]):
    '''
    递归函数，遍历该文档目录和子目录下的所有文件，获取其path
    '''
    
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):   # not a dir
            all_files.append(root_path + '/' + file)
        else:  # is a dir
            get_file((root_path+'/'+file),all_files)
    return all_files



def Receive():
    path = 'D:/Desktop/1'
    # path = 'D:/Desktop/2'
    file_path = get_file(path)
    # file_name = os.listdir(path)
    for f in file_path:
        print(f)
        cap = cv2.VideoCapture(f)
        while (True):
            ret, frame = cap.read()]
    print (cap,ret,frame)

result = Receive()
print(result)
c = 1
timeRate = 1  # 截取视频帧的时间间隔
def Display(result):  
    FPS = cap.get(5)
    if ret:
        frameRate = int(FPS) * timeRate  # 因为cap.get(5)获取的帧数不是整数，所以需要取整一下（向下取整用int，四舍五入用round，向上取整需要用math模块的ceil()方法）
        if (c % frameRate == 0):
            # 显示截取的帧图片、保存截取帧到本地
            t = time.time()
            millis = int(round(time.time() * 1000))
            fra = str(c)
            print(fra) 
            name = f.split('/')[-1].split('.')[0]
            cv2.imwrite("G:/observer_compute_intelligence/data/RawData/20220408/images/images0/%s_%s.jpg" % (name, fra) ,frame)
        c += 1
        cv2.waitKey(0)
    
    else:
        print("所有帧都已经保存完成")
        break


cap.release()


if __name__=='__main__':
    p1=threading.Thread(target=Receive)
    p2 = threading.Thread(target=Display)
    p1.start()
    p2.start()