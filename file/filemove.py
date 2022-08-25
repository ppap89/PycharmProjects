import shutil
import os
import time


count = 0
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


path = 'G:/observer_compute_intelligence/data/RawData/20220419/videos_parking_images'
# path = 'D:/Desktop/2'
file_path = get_file(path)
#file_name = os.listdir(path)
new_path = 'G:/observer_compute_intelligence/data/Rawdata/parking_images'
for f in file_path:
    print(f)
    #count = count + 1
    # if count > 3298:
    try:
        shutil.copy(os.path.join(f), os.path.join(new_path))   # 文件移动
    except:
        continue
    #else:
     #   path2 = 'G:/observer_compute_intelligence/data/youtubedl/image/image03/0/' 
      #  try:
       #     shutil.copy(os.path.join(f), os.path.join(path2))   # 文件移动
        #except:
         #   continue
    #  print(f.strip()[0:7])
    
    # with open("D:/Desktop/image_name_2.txt", "a") as txt:
    #     txt.write('\n'+ f'{f}')
        # try:
        #     # millis = int(round(time.time() * 1000))
        #     # shutil.copy(os.path.join(f), "W:/observer_compute_intelligence/data/RowData/YuHang2/images2/2/"+ f'{millis}' +".jpg") # 文件复制+重命名
        #     # if f.strip()[0:9] == 'bike_lane':
        #     #     print(f)
        
        # except:
        #     continue
           
  

  