import csv
import cv2
import os
import random
# 当前子数据集的标注文件地址
annotation_path = r"D:/Desktop/image_v6/content2/validation/labels/detections_ces.csv"
# 图片文件夹路径
image_path = r"D:/Desktop/image_v6/content2/validation/data"
# 类别缩写文件
class_name_csv = r"D:/Desktop/image_v6/content2/validation/metadata/classes.csv"
# 保存路径
save_file = r"D:/Desktop/image_v6/content2/validation/result/"
annotation_data = []
with open(annotation_path,"r") as f:
    annotation_files = csv.reader(f)
    print(annotation_files)
    for data in annotation_files:
        if  data[2] == "/m/01jfm_" :
            annotation_data.append(data)
images_name_list = os.listdir(image_path)
images_path_list = [os.path.join(image_path,image_name) for image_name in images_name_list]

classes_dict = {}
with open(class_name_csv,"r") as f:
    annotation_files = csv.reader(f)
    for data in annotation_files:
        classes_dict[data[0]] = data[1]
print(classes_dict)

import numpy as np
np.random.seed(12)
np.random.shuffle(images_path_list)
np.random.seed(12)
np.random.shuffle(images_name_list)

for i, image_path in enumerate(images_path_list):
    image_src = cv2.imread(image_path)
    image_name = images_name_list[i].split(".")[0]
    image_row = image_src.shape[0]
    image_col = image_src.shape[1]
    #print(image_row,image_col)
    for image_annotation in annotation_data:
        if image_annotation[0] == image_name:
            x = float(image_annotation[4]) * image_col
            x2 = float(image_annotation[5]) * image_col
            y = float(image_annotation[6]) * image_row
            y2 = float(image_annotation[7]) * image_row
            class_name = classes_dict[image_annotation[2]]
            cv2.rectangle(image_src,(int(x),int(y)),(int(x2),int(y2)),[0,255,0],2)
            cv2.putText(image_src,class_name,(int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 255), 2)
  #  cv2.imshow("src",image_src)
    cv2.imwrite(save_file + image_name + ".jpg",image_src)
    cv2.waitKey(1000)
