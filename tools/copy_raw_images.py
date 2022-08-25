
import pandas as pd
import os
import random
import shutil

df = pd.read_csv("./data_index_v1.4.csv", index_col=0, dtype={"imageName":str, "rawDataId":str, "currentLane"
:str, "detection":str, "segmentation":str, "laneBoundary":str, "invalid":str, "dataset_type":str})


# 获取符合条件的所有图片名称
# f_list = df.loc[df["segmentation"].isna() & (df['dataset_type'] == 'train') & (df['currentLane'] == 'crosswalk'),'imageName'].values.tolist()
f_list = df.loc[df['dataset_type'] == 'test']['imageName'].values.tolist()

# 从中随机抽取需求量+300的图片
# f_list = df.loc[df["laneBoundary"].isna(), :]["imageName"].values.tolist()
#sample_file_list = random.sample(f_list, 2)

rawImages = "\\\\OBTECH-NAS-001\\Share\\data\\RawData\\{}\\images"

def copy_image(image_name):
    rawdataid = df.loc[df["imageName"] == image_name, "rawDataId"].values[0]
    shutil.copy(os.path.join(rawImages.format(rawdataid), image_name), os.path.join("\\\\OBTECH-NAS-001\\Share\\data\\DevData\\37\\images", image_name))


for i in f_list:
    copy_image(i)

'''
# 人工筛选去除300张图片后，再执行！
# 更新csv数据信息并保存
import pandas as pd
import os
import shutil
df = pd.read_csv("data_index_v1.3.csv", index_col=0, dtype={"imageName":str,"rawDataId":str,"currentLane"
:str,"detection":str,"segmentation":str,"laneBoundary":str,"invalid":str,"dataset_type":str})
#f_list = df.loc[(df['dataset_type'] == 'validate') & (df['laneBoundary'] == '29'),'imageName'].values.tolist()
#rawImages = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (3)"
#def copy_image(image_name):
#    rawdataid = df.loc[df["imageName"] == image_name, "rawDataId"].values[0]
#    shutil.copy(os.path.join(rawImages.format(rawdataid), image_name), os.path.join("C:\\Users\\Administrator\\Desktop\\新建文件夹 (4)", image_name))


#for i in f_list:
#    copy_image(i)
path = "\\\\OBTECH-NAS-001\\Share\\data\\DevData\\36\\images"
#path = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (3)"
df.loc[df["imageName"].isin(os.listdir(path)), "laneBoundary"] = "36"

df.to_csv("data_index_v1.4.csv")'''
