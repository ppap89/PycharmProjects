import json

f=open("D:/Desktop/image_v6/content2/validation/labels/detections.csv","r",encoding='gbk') #文件所在位置
ls=[]
for line in f:
        line = line.replace("\n", "")
        ls.append(line.split(","))

f.close()
fw=open("D:/Desktop/image_v6/content2/validation/labels/detections.json","w",encoding='utf-8')#文件所在位置
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
a = json.dumps(ls[1:],sort_keys=True,indent=4,ensure_ascii=False)
print(a)
fw.write(a)
fw.close()

