import argparse
import pylab as plt
import matplotlib
import cv2
import torch

from detect import detect

src = 'E:\\project\\data\\img\\yolo7testimg\\b.jpg'

parser = argparse.ArgumentParser()
opt = parser.parse_args()
opt.weights = 'yolov7.pt'
opt.img_size = 1920
opt.source = src
opt.view_img = False
opt.save_txt = False
opt.save_conf = False
opt.classes = None  # None才會顯示框線
opt.no_trace = False
opt.nosave = False  # False才會儲存
opt.project = 'runs/detect'
opt.name = 'exp'
opt.exist_ok = True  # True才不會一直新增目錄
# yolo7只能在有 GPU的電腦執行
opt.device = '0'  # 使用 GPU 0裝置
opt.augment = False
opt.conf_thres = 0.25
opt.iou_thres = 0.45
opt.agnostic_nms = False
opt.update = False

with torch.no_grad():
    img = detect(myopt=opt)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
matplotlib.use('qt5agg')  # 改成 qt5agg模式才可以顯示圖片
plt.imshow(img)
plt.axis('off')
plt.show()

# 更改 detect, 使 python可以傳入參數, 也保留原本由命令提示字元傳入參數的功能
#   def detect(save_img=False, myopt=None):
#       global opt
#       if myopt is not None : opt=myopt
#       ...
#       return im0
