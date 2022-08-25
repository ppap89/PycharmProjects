from xml.dom import minidom
from xml.etree import ElementTree as et
import shutil
import os
# xml1 = minidom.parse('D:/Desktop/wallpic/task_semanticseg1000-2022_03_23_09_21_41-cvat for images 1.1/annotations.xml')


# images = xml1.getElementsByTagName("image")  # 获取节点列表


# for i in range(len(images)):  # 获取节点属性
#     print(images[i])
#     for t1 in images[i].iter('label'):
#         print(t1.text)
#     image_name =  images[i].getAttribute("name").split("/")[-1]
#     print(images[i].getA5ttribute("polygon"))
#         # print(image_name)

# #   shutil.copy(os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\38\\images", image_name),
# #               os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\39\\images", image_name))
# # print("all selected images were copied")

import xml.etree.ElementTree as ET
 
tree = ET.parse('D:/Desktop/wallpic/task_semanticseg1000-2022_03_23_09_21_41-cvat for images 1.1/annotations.xml')
root = tree.getroot()

print(root.tag ,root.attrib)

for child in root:
    for t in child .iter('id'):
     print(t.text)
    # print(child.tag , child.attrib)
    # print(child[0][0].tag)


# for t in root.iter('name'):
#     print(t.text)



# print(root[0][1].text)


# for image in root.iter('name'):
#     print(image.attrib)