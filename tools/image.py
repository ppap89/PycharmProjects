# -*- coding:utf-8 -*-
import json
import shutil
import os
import xml.etree.ElementTree as ET

from xml.dom import minidom

'''
xml1 = minidom.parse('C:/Users/Administrator/Desktop/annotations_raw.xml')
images = xml1.getElementsByTagName("image")  # 获取节点列表

list = []
for i in range(len(images)):  # 获取节点属性
    image_name =  images[i].getAttribute("name").split("/")[-1]
    list.append(image_name)
     # shutil.copy(os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\38\\images", image_name),
                    # os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\39\\images", image_name))
print("all selected images were copied")'''

xml1 = ET.parse('//OBTECH-NAS-001/Share/data/DevData/39/annotations/annotations_raw.xml')
images = xml1.getroot()
list = []

for image in images.iter('image'):
    image_name = image.get("name").split("/")[-1]
    if image.find("points") is not None:
        list.append(image_name)
        shutil.copy(os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\38\\images", image_name),
                    os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\39\\images", image_name))
print("all selected images were copied")

filepath = "\\\\OBTECH-NAS-001\\Share\\data\\DevData\\39\\images"
imagename_list = os.listdir(filepath)
print(imagename_list)
path = "\\\\OBTECH-NAS-001\\Share\\data\\DevData\\38\\annotations"
with open(os.path.join(path, "hem.json"), "r") as f:
    raw_annotations = json.loads(f.read())  # json解码json文件转化成python数据类型

images = []
annotations = []
image_index = 0
annotation_index = 0
for item in raw_annotations["images"]:
    if item["file_name"] in imagename_list:
        temp = {
                "id": image_index,
                "file_name": item["file_name"],
                "width": item["width"],
                "height": item["height"]
        }
        # 筛选images_list中的图片数据并保存至temp中
        images.append(temp)  # 添加图片数据
        image_index += 1  # 自动编号
        for annotation in raw_annotations["annotations"]:
            if annotation["image_id"] == item["id"] :
                temp2 = {
                    "id": annotation_index,
                    "image_id": temp["id"],
                    "category_id": annotation["category_id"],
                    "segmentation": [],
                    "area": annotation["area"],
                    "bbox": annotation["bbox"],
                    "iscrowd": annotation["iscrowd"]
                    }
                annotations.append(temp2)
                annotation_index += 1
    
new_annotations = {
    "license": raw_annotations["license"],
    "info": raw_annotations["info"],
    "categories": raw_annotations["categories"],
    "images": images,
    "annotations": annotations
}
with open(os.path.join("C:\\Users\\Administrator\\Desktop","instance_default_raw6.json"), "w") as f:
    json.dump(new_annotations, f)  # 转化成json


# f = open("C:\\Users\\Administrator\\Desktop\\instance_default_raw5.json",'r')
# data =json.loads(f.read())
