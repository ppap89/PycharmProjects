import csv
from tqdm import tqdm
import os
# 标注文件路径
csv_file_path = r"D:/Desktop/image_v6/content2/validation/labels/detections.csv"
# 图像文件夹路径
images_file_path = r"D:/Desktop/image_v6/content2/validation/data"
images_name = os.listdir(images_file_path)
images_name = [x.split(".")[0] for x in images_name]

# 保存标注文件路径
data_annotation_csv = r"D:/Desktop/image_v6/content2/validation/labels/detections_ces.csv"
with open(csv_file_path, 'r', encoding='utf-8') as f:
    with open(data_annotation_csv, "w", encoding='utf-8') as ff:
        csv_f = csv.reader(f)
        bar = tqdm(csv_f)
        for row in bar:
            if row[0] in images_name:
                # print("get image {}".format(row[0]))
                for index in range(len(row)):
                    ff.write(row[index])
                    if (index != (len(row) - 1)):
                        ff.write(",")
                ff.write("\n")
