# 车辆与行人的目标检测
## 任务简述
   对交通场景下的图像或视频进行行人与车辆的目标检测
## 数据集

| 数据集               | 类别                 | 图像分辨率               | 图像的长宽比                  | 训练集的数量             |          测试集的数量 |
| :------| :------ | :------ | :------| :------|:------|
|VOC2007              |Person: person<br>Vehicle: bicycle, bus, car, motorbike|图片的像素尺寸大小不一|长宽比不唯一，但不会太大也不会太小|person 2008<br>bicycle 243<br>bus 186<br>car 713<br>motorbike  245|person 2007<br>bicycle 239<br>bus 174<br>car 721<br>motorbike 222|
|KITTI|Car:Truck, Van, Tram, Car<br>Person:Person_sitting, Cyclist, Pedestrian|1242*375|3.4:1|7481|7518|



## 评价指标
速度指标：FPS(在同一硬件下，每秒处理图片的数量或者处理每张图片所需要的时间)<br>
模型精度性能指标：mAP

本任务需要检测行人和车辆两个类别，选取的是公共数据集VOC2007中的person类和vehicle类和KITTI中的car和person。我们采用mAP的方式来评价精度。对于行人和车辆会分别计算AP，然后取平均值两个AP的均值作为结果。另外任务对速度也有一定的要求，我们采用FPS的评测方法对速度进行评估。

