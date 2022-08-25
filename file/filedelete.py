
import os
import shutil

def get_file(root_path,all_files=[]):
    '''
    递归函数，遍历该文档目录和子目录下的所有文件，获取其path
    '''
    
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):   # not a dir
            all_files.append(root_path + '/' + file)
        else:  # is a dir
            get_file((root_path+'/'+file),all_files)
    return all_files

path = 'E:\\currentlane_nonmotorroad\\LowPerspectiveData\\'
# path = 'D:/Desktop/2'
# file_path = get_file(path)
dirname = os.listdir(path)
# print(file_path)
for f in dirname:
    try:
        
        shutil.move("E:\\currentlane_nonmotorroad\\images\\%s"% f,"E:\\currentlane_nonmotorroad\\1\\%s"% f)
    except:
        continue