import json
import os
from pickle import FALSE

# path = "G:/observer_compute_intelligence/data/RowData/PoorInferAHD"
# with open(os.path.join(path, "instance.json"), "r") as f:
#     raw_annotations = json.loads(f.read())  # json解码json文件转化成python数据类型


path = "D:/Desktop/task_ahd poor infer instance segmentation 2000 46-2022_01_17_06_02_41-coco 1.0/annotations"
with open(os.path.join(path, "instances_default.json"), "r") as f:
    raw_annotations = json.loads(f.read())
# path = 'G:/observer_compute_intelligence/data/RowData/PoorInferAHD/PoorInferAHDSelect'
# # path = 'D:/Desktop/2'
# file_name = os.listdir(path)


images = []
annotations = []
image_index = 0
annotation_index = 0

for item in raw_annotations["images"]:
    # if item["file_name"] in file_name:
    #     print(item["file_name"])
    temp = {    
            "id": image_index,
            "width": item["width"],
            "height": item["height"],
            "file_name": item["file_name"],
            'license': item['license'],
            'flickr_url':item['flickr_url'],
            "coco_url":item["coco_url"],
            "date_captured":item["date_captured"]
            # "date_captured": 0 
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
                "segmentation": annotation['segmentation'],
                "area": annotation["area"],
                "bbox": annotation["bbox"],
                "iscrowd": annotation["iscrowd"],
                "attributes": annotation["attributes"]
                # "attributes" : {"occluded": false}
                }
            annotations.append(temp2)
            annotation_index += 1
    
new_annotations = {
    #  "licenses": [{"name": "", "id": 0, "url": ""}],
    "licenses": raw_annotations["licenses"],
    "info": raw_annotations["info"],
    # "info":[{"contributor": "", "date_created": "", "description": "", "url": "", "version": "", "year": ""}],
    "categories": raw_annotations["categories"],
    "images": images,
    "annotations": annotations
}
with open(os.path.join("D:\\Desktop","instance_default2.json"), "w") as f:
    json.dump(new_annotations, f)  # 转化成json


# f = open("C:\\Users\\Administrator\\Desktop\\instance_default_raw5.json",'r')
# data =json.loads(f.read())
