# Python 根Python 根据文件名新建文件夹并移动到文件夹里面据文件名新建文件夹并移动到文件夹里面
import os
import shutil
 
 
def main():
    path = r"D:/Desktop/新建文件夹 (3)"
    newPath = "D:/Desktop/新建文件夹 (3)/"
    num = 1
    
    for (root, dirs, files) in os.walk(path):
        for filename in files:
            singleFile = os.path.join(root, filename)
            # res = os.path.splitext(filename)
            s = '%04d' % num
            newFileDirs = newPath + "2021_06_10_drive_" + f'{s}' + "_sync" + "/";
            os.mkdir(newFileDirs)
            print(newFileDirs)
            lastpath = newFileDirs + "image_02"
            print(lastpath)
            # 文件不存在则新建文件
            # if not os.path.exists(lastpath):
            os.mkdir(lastpath)
            # 将当前文件移动到新建的文件夹里面
            shutil.move(singleFile, lastpath + "/" + filename)
            num += 1
    pass
 
 
if __name__ == '__main__':
    main()



