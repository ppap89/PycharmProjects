"""
date: 2021-09-30

points classification toolkit for PointSup

usage:
    1. for annotation:
    python pointsup_annotation.py --json_file path/to/data.json --data_root path/to/datadir [--scale 0.8] [--point_num 10]

    2. for visualize:
    python pointsup_annotation.py --json_file path/to/data.json --data_root path/to/datadir
                                  --visualize [--scale 0.8] [--start 10]

keys:
for annotation:
- key 'p' for positive class
- key 'n' for negative class
- key 'r' for relabel all points in an annotation
- key 'q' or 'Esc' for exit

for visualize:
- key 'u' for show previous bbox and points
- key 't' for show previous image
"""
# encoding=utf-8
import os
import cv2
import time
import json
import argparse
import numpy as np
from pathlib import Path
from copy import deepcopy
from collections import defaultdict


class COCO:
    def __init__(self, annotation_file=None, logs=True):
        """
        Constructor of Microsoft COCO helper class for reading and visualizing annotations.
        :param annotation_file (str): location of annotation file
        :param image_folder (str): location to the folder that hosts images.
        :return:
        """
        self.logs = logs

        # load dataset
        self.dataset, self.anns, self.cats, self.imgs = dict(), dict(), dict(), dict()
        self.imgToAnns, self.catToImgs = defaultdict(list), defaultdict(list)
        if annotation_file is not None:
            print('loading annotations into memory...') if self.logs else None
            tic = time.time()
            dataset = json.load(open(annotation_file, 'r'))
            assert type(dataset) == dict, 'annotation file format {} not supported'.format(type(dataset))
            print('Done (t={:0.2f}s)'.format(time.time() - tic)) if self.logs else None
            self.dataset = dataset
            self.createIndex()

    def createIndex(self):
        # create index
        print('creating index...') if self.logs else None
        anns, cats, imgs = {}, {}, {}
        imgToAnns, catToImgs = defaultdict(list), defaultdict(list)
        if 'annotations' in self.dataset:
            for ann in self.dataset['annotations']:
                imgToAnns[ann['image_id']].append(ann)
                anns[ann['id']] = ann

        if 'images' in self.dataset:
            for img in self.dataset['images']:
                imgs[img['id']] = img

        if 'categories' in self.dataset:
            for cat in self.dataset['categories']:
                cats[cat['id']] = cat

        if 'annotations' in self.dataset and 'categories' in self.dataset:
            for ann in self.dataset['annotations']:
                catToImgs[ann['category_id']].append(ann['image_id'])
            # set to list
            catToImgs.default_factory = list
            for cid, setobj in catToImgs.items():
                catToImgs[cid] = list(set(setobj))

        print('index created!') if self.logs else None

        # create class members
        self.anns = anns
        self.imgToAnns = imgToAnns
        self.catToImgs = catToImgs
        self.imgs = imgs
        self.cats = cats


class PointSupAnnotate(object):
    """
    points classify for PointSup

    usage:
        1. for annotation:
        python pointsup_annotation.py --json_file path/to/data.json --data_root path/to/datadir [--scale 0.8] [--point_num 10]

        2. for visualize:
        python pointsup_annotation.py --json_file path/to/data.json --data_root path/to/datadir
                                      --visualize [--scale 0.8] [--start 10]

    key description:
        # annotation:
        - key 'p' for positive class (you can set self.positive_key for your like key)
        - key 'n' for negative class (you can set self.positive_key for your like key)
        - key 'r' for relabel all points in an annotation (you can set self.positive_key for your like key)
        - key 'q' or 'Esc' for exit

        # visualize
        - key 'u' for show previous bbox and points
        - key 't' for show previous image

    params:
        json_file: (str) json file path
        data_root: (str) image data directory
        scale: (float) show the image with scale
        point_num: (int) point number for each annotation
    """
    def __init__(self, json_file, data_root, scale=1.0, point_num=10, visualize=False, start=0):
        self.json_file = Path(json_file)
        self.data_root = Path(data_root)
        self.point_num = point_num
        self.scale = scale
        self.visualize = visualize
        self.start = start

        assert self.json_file.exists()
        assert self.data_root.exists() and self.data_root.exists()
        assert self.point_num > 0
        assert self.scale > 0

        self.coco = COCO(str(self.json_file))

        if not visualize:
            # key config
            self.positive_key = ord('p')    # positive label
            self.negative_key = ord('n')    # negative label
            self.relabel_key = ord('r')     # when show all point in an annotation, you can relabel all points use this key

            self.temp_dir = Path(f"temp_pointSup/{str(self.json_file.stem)}")
            if not self.temp_dir.exists():
                self.temp_dir.mkdir(parents=True, exist_ok=True)
            # annotated list
            if self.temp_dir.exists():
                self.annotated = [int(js.stem) for js in self.temp_dir.glob("*.json")]
            else:
                self.annotated = []

            # unannotate list
            self.unannotate = list(self.coco.imgs.keys())
            if len(self.annotated) != 0:
                for imid in self.annotated:
                    self.unannotate.remove(imid)

    def annotate(self):
        total = len(self.coco.dataset["images"])

        for img_id in self.unannotate:
            # one image
            img_obj = self.coco.imgs[img_id]
            img_path = self.data_root / img_obj["file_name"]
            assert img_path.exists(), f"image {str(img_path)} does not exist."
            print(img_path)
            image0 = cv2.imread(str(img_path))
            img_size = image0.shape[:2]
            image0 = cv2.resize(image0, (0, 0), fx=self.scale, fy=self.scale)

            anns = self.coco.imgToAnns[img_id]
            annotateds = []
            for ai, ann in enumerate(anns):
                # all annotations in an image
                image1 = deepcopy(image0)
                bbox = ann["bbox"]
                name = self.coco.cats[ann["category_id"]]["name"]
                image1 = self._draw_bbox(image1, bbox, name)
                cv2.putText(image1, f"Total: {len(self.annotated)}/{total}", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
                cv2.putText(image1, f"Anno: {ai}/{len(anns)}", (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

                # ramdom generate points
                point_coords = self.random_point_from_bbox(bbox, img_size)
                if point_coords is None:
                    continue

                while True:
                    # label points
                    point_labels = self._label_point(image1, point_coords)

                    # show all labeled point, and determine whether it is necessary to relabel
                    image2 = deepcopy(image1)
                    image2 = self._draw_bbox_and_points(image2, bbox, point_coords, point_labels)
                    cv2.imshow("PointSup Annotation Tool", image2)
                    c = cv2.waitKey()
                    if c == self.relabel_key:
                        continue
                    elif c == 27 or c == ord('q'):  # exit
                        exit(0)
                    else:
                        break

                # save point coords and labels of one object
                ann["point_coords"] = point_coords.tolist()
                ann["point_labels"] = point_labels
                if "segmentation" in ann.keys() and len(ann["segmentation"]) != 0:
                    ann["segmentation"] = []
                annotateds.append(ann)

            # save a image result for cache
            cache_json_path = self.temp_dir / f"{img_id}.json"
            json.dump(annotateds, open(cache_json_path, 'w'))
            self.annotated.append(img_id)
        
        # finished, merge all cache json to a json file, and save
        if len(self.annotated) == total:
            self._save()
        else:
            print("\031[1;33mSome error happen, please rerun the program./033[0m")

    def _label_point(self, image, point_coords):
        i = 0
        point_labels = []
        while i < self.point_num:
            # for each point
            point_coord = point_coords[i]
            image2 = deepcopy(image)
            cv2.circle(image2, (int(point_coord[0] * self.scale), int(point_coord[1] * self.scale)), 2, (0, 0, 255), -1)
            cv2.circle(image2, (int(point_coord[0] * self.scale), int(point_coord[1] * self.scale)), 20, (0, 255, 0), 1)
            cv2.putText(image2, f"Point: {i + 1}/{self.point_num}", (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0),
                        1)

            cv2.imshow("PointSup Annotation Tool", image2)
            c = cv2.waitKey()
            if c == 27 or c == ord('q'):  # exit
                exit(0)
            elif c == self.positive_key:
                # positive point
                point_labels.append(1)
                i += 1
            elif c == self.negative_key:
                # negative point
                point_labels.append(0)
                i += 1
            else:
                # press the other key, do nothing
                continue

        return point_labels

    def _draw_bbox(self, image, bbox, name=None, lt=2):
        assert len(bbox) == 4
        x0, y0, w, h = bbox
        x1 = int((x0 + w) * self.scale)
        y1 = int((y0 + h) * self.scale)
        x0 = int(x0 * self.scale)
        y0 = int(y0 * self.scale)
        cv2.rectangle(image, (x0, y0), (x1, y1), (255, 0, 0), lt)

        if name is not None:
            cv2.putText(image, name, (x0, y0-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        return image
    
    def _draw_bbox_and_points(self, image, bbox, point_coords, point_labels, name=None, pr=2, cr=10, lt=2):
        image = self._draw_bbox(image, bbox, name=name, lt=lt)
        assert len(point_coords) == len(point_labels)
        for i in range(len(point_coords)):
            point_coord = point_coords[i]
            point_label = point_labels[i]
            if point_label == 0:
                # negative color
                color = (255, 0, 0)
            elif point_label == 1:
                # positive color
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)
                print("error label")
            cv2.circle(image, (int(point_coord[0] * self.scale), int(point_coord[1] * self.scale)), pr, color, -1)
            cv2.circle(image, (int(point_coord[0] * self.scale), int(point_coord[1] * self.scale)), cr, color, 1)
        return image

    def random_point_from_bbox(self, box, image_size):
        # check bbox is right(in image)
        if box[0] < 0 or box[1] < 0:
            return None

        # image_size: [h, w]
        h, w = image_size
        point_coords_wrt_image = np.random.rand(self.point_num, 2)
        point_coords_wrt_image[:, 0] = point_coords_wrt_image[:, 0] * box[2]
        point_coords_wrt_image[:, 1] = point_coords_wrt_image[:, 1] * box[3]
        point_coords_wrt_image[:, 0] += box[0]
        point_coords_wrt_image[:, 1] += box[1]
        # round to integer coordinates
        point_coords_wrt_image = np.floor(point_coords_wrt_image).astype(int)
        # get labels
        assert (point_coords_wrt_image >= 0).all(), (point_coords_wrt_image, image_size)
        assert (point_coords_wrt_image[:, 0] < w).all(), (point_coords_wrt_image, image_size)
        assert (point_coords_wrt_image[:, 1] < h).all(), (point_coords_wrt_image, image_size)

        return point_coords_wrt_image

    def _save(self):
        json_files = list(self.temp_dir.glob("*.json"))
        if len(json_files) != len(self.coco.dataset["images"]):
            print("\031[1;33mSome error happen, please rerun the program./033[0m")
            exit(0)

        annotations_list = []
        for json_file in json_files:
            annos = json.load(open(str(json_file)))
            annotations_list.extend(annos)
        self.coco.dataset["annotations"] = annotations_list

        print("saving file ...")
        new_json = self.json_file.parent / (str(self.json_file.stem) + f"_pointsup_n{self.point_num}_without_masks.json")
        with open(new_json, 'w') as f:
            json.dump(self.coco.dataset, f)
        print(f"new JSON file saved in {new_json}.")

    def show(self):
        """
        show pointsup points one by one

        keys:
            -u: show previous bbox and points
            -t: show previous image
        """
        img_ids = sorted(list(self.coco.imgs.keys()))
        
        img_count = self.start
        while img_count < len(img_ids):
            # imid = img_obj["id"]
            imid = img_ids[img_count]
            img_obj = self.coco.imgs[imid]
            img_path = self.data_root / img_obj["file_name"]
            image0 = cv2.imread(str(img_path))
            image0 = cv2.resize(image0, (0, 0), fx=self.scale, fy=self.scale)
            print(imid, img_path)
            anns = self.coco.imgToAnns[imid]
            ann_count = 0
            while ann_count < len(anns):
                image1 = deepcopy(image0)
                ann = anns[ann_count]

                assert "point_coords" in ann
                assert "point_labels" in ann

                cv2.putText(image1, f"Total: {img_count}/{len(img_ids)}", (0, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
                cv2.putText(image1, f"Anno: {ann_count}/{len(anns)}", (0, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

                bbox = ann["bbox"]
                name = self.coco.cats[ann["category_id"]]["name"]
                point_coords = ann["point_coords"]
                point_labels = ann["point_labels"]
                self._draw_bbox_and_points(image1, bbox, point_coords, point_labels, name=name, cr=0, pr=3)

                cv2.imshow("PointSup Visualize Tool", image1)
                c = cv2.waitKey()
                if c == 27 or c == ord('q'):
                    exit(0)
                elif c == ord('u'):
                    ann_count -= 1
                    if ann_count < 0:
                        img_count -= 2
                        ann_count = 0
                        if img_count < -1:
                            img_count = 0
                        break
                elif c == ord('t'):
                    img_count -= 2
                    ann_count = 0
                    if img_count < -1:
                        img_count = 0
                    break
                elif c == ord('a'):
                    F1 = open('C:\\Users\\Administrator\\Desktop\\1\\annotation1-check1.txt', 'a')
                    F1.write(str(imid))
                    F1.write('\n')
                    print('{} already written..,id:{}'.format(img_path,imid))
                else:
                    ann_count += 1

            img_count += 1

    def __call__(self, *args, **kwargs):
        if self.visualize:
            self.show()
        else:
            self.annotate()


if __name__ == '__main__':
    # 0 for command line, 1 for IDE
    method = 0

    if method == 0:
        # for command line run
        # 使用方法：python pointsup_annotation.py --json_file path/to/data.json --data_root path/to/datadir --scale 0.8
        parser = argparse.ArgumentParser(description="Annotate pointsup")
        parser.add_argument("--json_file", type=str)
        parser.add_argument("--data_root", type=str)
        parser.add_argument("--point_num", type=int, default=10)
        parser.add_argument("--scale", type=float, default=0.8)
        parser.add_argument("--visualize", action="store_true")
        parser.add_argument("--start", type=int, default=0)
        args = parser.parse_args()

        psa = PointSupAnnotate(args.json_file, args.data_root,
                               scale=args.scale,
                               point_num=args.point_num,
                               visualize=args.visualize,
                               start=args.start)
        psa()
    elif method == 1:
        # for IDE run
        # TODO: 请手动修改下面两个路径
        # json_file = "./test.json"
        # data_root = "/mnt/Storage/datasets/cityscapes/leftImg8bit"
        json_file = "/mnt/nfs/share/data/DevData/22/annotations/instances_default_pointsup_n10_without_masks.json"
        data_root = "/mnt/nfs/share/data"
        img_scale = 0.8
        visualize = False       # False for annotation
        start = 0

        psa = PointSupAnnotate(json_file, data_root, scale=img_scale, visualize=visualize, start=start)
        psa()
