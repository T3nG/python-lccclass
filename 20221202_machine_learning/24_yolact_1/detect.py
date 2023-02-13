import time
from collections import defaultdict

import cv2
import numpy as np
import torch
from torch.backends import cudnn

from data import set_cfg, cfg, COLORS
from layers.output_utils import postprocess
from utils import timer
from utils.augmentations import FastBaseTransform
from yolact import Yolact


def detect(model, img_path):
    with torch.no_grad():
        image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        image = cv2.resize(image, (800,600), interpolation=cv2.INTER_LINEAR)
        image, result = detect_image(model, image)
        return image, result

def detect_image(model, image):
    model.detect.use_fast_nms = True  # 快速偵測
    model.detect.use_cross_class_nms = False
    cfg.mask_proto_debug = False
    frame = torch.from_numpy(image).cuda().float()
    batch = FastBaseTransform()(frame.unsqueeze(0))
    preds = model(batch)
    return prep_display(preds, frame)  # 標示框線及填滿顏色

# 複製 eval.py 的 get_color函數, 修改
def get_color(j, classes, class_color, on_gpu=None):
    color_cache = defaultdict(lambda: {})
    color_idx = (classes[j] * 5 if class_color else j * 5) % len(COLORS)

    if on_gpu is not None and color_idx in color_cache[on_gpu]:
        return color_cache[on_gpu][color_idx]
    else:
        color = COLORS[color_idx]
        color = (color[2], color[1], color[0])
        if on_gpu is not None:
            color = torch.Tensor(color).to(on_gpu).float() / 255.
            color_cache[on_gpu][color_idx] = color
        return color

# 複製eval.py 裡的 prep_display函數, 修改
def prep_display(dets_out, img, class_color=False, mask_alpha=0.25):
    score_threshold = 0.3
    crop = False
    top_k = 100
    img_gpu = img / 255.0
    h, w, _ = img.shape
    with timer.env('Postprocess'):
        save = cfg.rescore_bbox
        cfg.rescore_bbox = True
        t = postprocess(dets_out, w, h, visualize_lincomb=False,
                        crop_masks=crop,
                        score_threshold=score_threshold)
        cfg.rescore_bbox = save
    with timer.env('Copy'):
        idx = t[1].argsort(0, descending=True)[:top_k]
        if cfg.eval_mask_branch:
            masks = t[3][idx]
        classes, scores, boxes = [x[idx].cpu().numpy() for x in t[:3]]
    num_dets_to_consider = min(top_k, classes.shape[0])
    for j in range(num_dets_to_consider):
        if scores[j] < score_threshold:
            num_dets_to_consider = j
            break
    if cfg.eval_mask_branch and num_dets_to_consider > 0:
        masks = masks[:num_dets_to_consider, :, :, None]
        colors = torch.cat(
            [get_color(j, classes, class_color, on_gpu=img_gpu.device.index).view(1, 1, 1, 3) for j in
             range(num_dets_to_consider)], dim=0)
        masks_color = masks.repeat(1, 1, 1, 3) * colors * mask_alpha
        inv_alph_masks = masks * (-mask_alpha) + 1
        masks_color_summand = masks_color[0]
        if num_dets_to_consider > 1:
            inv_alph_cumul = inv_alph_masks[:(num_dets_to_consider - 1)].cumprod(dim=0)
            masks_color_cumul = masks_color[1:] * inv_alph_cumul
            masks_color_summand += masks_color_cumul.sum(dim=0)
        img_gpu = img_gpu * inv_alph_masks.prod(dim=0) + masks_color_summand
    img_numpy = (img_gpu * 255).byte().cpu().numpy()
    # Thomas Add
    result = []
    display_scores = True
    for j in reversed(range(num_dets_to_consider)):
        x1, y1, x2, y2 = boxes[j, :]
        color = get_color(j, classes, class_color)
        score = scores[j]
        # 繪制框線
        cv2.rectangle(img_numpy, (x1, y1), (x2, y2), color, 1)
        # 顯示文字
        _class = cfg.dataset.class_names[classes[j]]
        text_str = '%s: %.2f' % (_class, score) if display_scores else _class
        # Thomas Add
        result.append([_class, score])

        font_face = cv2.FONT_HERSHEY_DUPLEX
        font_scale = 0.6
        font_thickness = 1
        text_w, text_h = cv2.getTextSize(text_str, font_face, font_scale, font_thickness)[0]
        text_pt = (x1, y1 - 3)
        text_color = [255, 255, 255]
        cv2.rectangle(img_numpy, (x1, y1), (x1 + text_w, y1 - text_h - 4), color, -1)
        cv2.putText(img_numpy, text_str, text_pt, font_face, font_scale, text_color, font_thickness, cv2.LINE_AA)
    return img_numpy, result


if __name__ == '__main__':
    img_path = 'test/elephant_01.jpg'
    config = 'animal_config'
    weights = 'weights/yolact_base_3999_8000.pth'

    set_cfg(config)
    cudnn.fastest=True
    torch.set_default_tensor_type('torch.cuda.FloatTensor')
    print('Loading Model ...', end='')
    model = Yolact()
    model.load_weights(weights)
    model.train(False)  # 關掉訓練, 表示要偵測圖片
    model = model.cuda()
    print('Done.')

    t1 = time.time()
    image, result = detect(model, img_path)
    t2 = time.time()
    print(f'偵測花費時間: {t2-t1}秒')
    print(result)

    cv2.imshow('test', image)
    cv2.waitKey(0)
