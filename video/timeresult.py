import datetime
import os
import time
from moviepy.editor import VideoFileClip
from numpy import append


def compute_video_time(path):  
    type = ('.flv', '.mp4', '.avi')   
    file_list = []
    for a, b, c in os.walk(path):
        for name in c:
            fname = os.path.join(a, name)
            if fname.endswith(type):
                file_list.append(fname)
    print("------开始计算时间------")
    ftime = 0.0
    count = 0
    for item in file_list:
        try:
            clip = VideoFileClip(item)
            ftime += clip.duration
            count = count + 1
            print("已完成%.2f" %((count / file_list.__len__()) * 100)+"%" )
            clip.reader.close()		# 防止出现错误：句柄无效
            clip.audio.reader.close_proc()
        except:
            print(item)
    print("总共%d个文件" %count)
    print(str(datetime.timedelta(seconds=ftime)))
    return ftime

list2 = []
filepath = "G:/observer_compute_intelligence/data/RawData"
imagename_list = os.listdir(filepath)
print(imagename_list)
for i  in imagename_list:
    if i[:4] == "2022":
        list2.append(i)
print(list2)

#list = ['20220210', '20220429144500', '20220715', '20220214', '20220222', '20220214~20220216', '20220225', '20220524', '20220523', '20220228', '20220301', '20220302', '20220303', '20220304', '20220322', '20220406', '20220324', '20220324_night', '20220329', '20220407', '20220408', '20220412', '20220407_night', '20220425', '20220414', '20220415', '20220418', '20220419', '20220429', '20220506', '20220525', '20220617_drover_test_400V', '20220623_200AI_night', '20220617_drover_test_400V_images']
timelist = []
if __name__ == '__main__':
    time_start = time.time()
   # for name in list:
   #     path = r"G:/observer_compute_intelligence/data/RawData/"+ name
    path = r"G:/observer_compute_intelligence/data/RawData/20220412"
    time_count = compute_video_time(path)
    print("总视频时间：", round(time_count, 2), "秒")
    print("总视频时间：", round(time_count / 60, 2), "分钟")
    print("总视频时间：", round(time_count / 60 / 60, 2), "小时")
    timelist.append(round(time_count / 60 / 60, 2))
    time_end = time.time()
    print("程序运行时间：", round(time_end - time_start, 2), "秒")
    print(timelist,sum(timelist))
