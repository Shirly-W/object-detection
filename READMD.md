##kitti转成voc数据集格式
tools.voc_format
##数据集kitti
config.base.yaml改数据集路径
model.config改class_num
dataset.VOC_dataset.py改CLASSES_NAME
## 推理可视化方法
python detect.py

读取test_images路径下的图片，将检测结果存到out_images中。

