import PIL.Image as img
import os

path = 'G:/observer_compute_intelligence/data/Germany/images/images1/sidewalk/1'
#file_path = get_file(path)
file_name = os.listdir(path)

path_old = "G:/observer_compute_intelligence/data/Germany/images/images1/sidewalk/1/"
path_new = "G:/observer_compute_intelligence/data/Germany/images/images1/sidewalk/1/"
filelist = os.listdir(path_old)
for f in file_name:
    print(f)
    im = img.open(path_old +  f)
#ng = im.transpose(img.ROTATE_180) #旋转 180 度角。
#ng = im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
    ng = im.transpose(img.FLIP_TOP_BOTTOM)  # 上下对换。
    ng.save(path_new + f)
    
           



