
import fiftyone as fo
import fiftyone.zoo as foz
import os
import pandas  as pd
from DatasetImporter import CSVImageClassificationDatasetImporter

pth_path = 'D:/Desktop/image_v6/content2/validation/labels/labels.json' # 这边的标签文件是用的前面下载的。
pth_path1 = "D:/Desktop/image_v6/content2/validation/data"  # 这个文件夹中是我之前下载的coco数据集中val系列的所有照片

# Import the dataset
dataset = fo.Dataset.from_dir(
    dataset_type=CSVImageClassificationDatasetImporter,
    data_path = pth_path1,
    labels_path = pth_path,
   # classes=["car"],
  #  only_matching=True,  # 指定仅下载符合条件的图片，即含有猫的图片
)
# dataset.name = "image1"

session = fo.launch_app(dataset)
session.wait()


