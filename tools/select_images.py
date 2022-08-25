# -*- coding: utf-8 -*-
import os
import shutil
import time
import pandas as pd
import json
import xml.etree.ElementTree as ET


if __name__ == "__main__":
    images_list = []
    path = "\\\\OBTECH-NAS-001\\Share\\data\\DevData\\34\\annotations"
    
    data_xml = ET.parse(os.path.join(path, "annotations.xml"))
    data_root = data_xml.getroot()
    for image in data_root.iter("image"):
        image_name = image.get("name").split("/")[-1]
        if image.find("points") is not None:
            images_list.append(image_name)
            # shutil.copy(os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\34\\images", image_name), os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\35\\images", image_name))
    print("all selected images were copied")
    time.sleep(20)

    with open(os.path.join(path, "hem2.json"), "r") as f:
        raw_annotations = json.loads(f.read())  #json解码json文件转化成python数据类型

    images = []
    annotations = []
    image_index = 0
    annotation_index = 0
    for item in raw_annotations["images"]:
        if item["file_name"] in images_list:
            temp = {
                "id": image_index,
                "file_name": item["file_name"],
                "width": item["width"],
                "height": item["height"]
            }
            #筛选images_list中的图片数据并保存至temp中
            images.append(temp)  #添加图片数据
            image_index += 1   #自动编号
            for annotation in raw_annotations["annotations"]:
                if annotation["image_id"] == item["id"]:
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
    with open(os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\35\\annotations", "instance_default_raw.json"), "w") as f:
        json.dump(new_annotations, f)   #转化成json

