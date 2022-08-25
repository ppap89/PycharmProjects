#import fiftyone as fo
#import fiftyone.zoo as foz

#dataset = foz.load_zoo_dataset("quickstart")
#session = fo.launch_app(dataset)

#
#
# import fiftyone as fo
# import fiftyone.zoo as foz
#
# # reference: https://voxel51.com/docs/fiftyone/tutorials/evaluate_detections.html
#
# datasets = foz.list_zoo_datasets()
# print("available datasets:", datasets)
#
# dataset = foz.load_zoo_dataset("coco-2017", split="validation", dataset_name="evaluate-detections-tutorial")
# dataset.persistent = True
# session = fo.launch_app(dataset)
#
# # print some information about the dataset
# print("dataset info:", dataset)
#
# # print a ground truth detection
# sample = dataset.first()
# print("ground truth:", sample.ground_truth.detections[0])
#
# session.wait()


# import fiftyone as fo
# import fiftyone.zoo as foz
#
# dataset = foz.load_zoo_dataset("quickstart")
#
# session = fo.launch_app(dataset,port = 5151)  # 没有指定port则默则5151
# session.wait()  # 官网给的示例没有这一句，记得加上，不然程序不会等待，在网页中看不到我们要的效果


import fiftyone as fo

# Create an empty dataset
dataset = fo.Dataset("test-dataset")

print(dataset)
h_app(dataset)