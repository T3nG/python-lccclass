# pip install Pillow opencv-python matplotlib
import pylab as plt
from PIL import Image, ImageDraw, ImageFont
from sdk.IvanCv import IvanCv as cv
img_path = 'E:\project\data\img\jpg\\1.jpg'

img = cv.read(img_path)
img = cv.resize(img, scale=0.2)
img = img[:, :, ::-1].copy()  # 轉RGB
h, w, _ = img.shape

pil = Image.fromarray(img)
draw = ImageDraw.Draw(pil, 'RGBA')  # 產生繪圖工具, 且是 RGBA格式, 像是畫筆

txt = 'Coron\n菲律賓科隆島\n2023/02/02'
font = ImageFont.truetype('simsun.ttc', 36)

# 偵測文字大小, 模擬文字框, 回傳左上及右下座標, 左上座標用不到
_, _, t_x2, t_y2 = draw.textbbox(xy=(0, 0), text=txt, font=font)

# 在圖的左上
# r_x1 = 0
# r_y1 = 0
# r_x2 = t_x2
# r_y2 = t_y2

# 在圖的左下
r_x1 = 0
r_y1 = h - (t_y2)
r_x2 = t_x2
r_y2 = h

# 在圖的右上
# r_x1 = w - t_x2
# r_y1 = 0
# r_x2 = w
# r_y2 = t_y2

# 在圖的右下
# r_x1 = w - t_x2
# r_y1 = h - t_y2
# r_x2 = w
# r_y2 = h

# draw.rectangle(x1, y1, x1, y2) 指定左上右下的點
# fill RGBA, A愈大愈不透明, 文字無法做半透明
draw.rectangle((r_x1, r_y1, r_x2, r_y2), fill=(150, 150, 255, 100))
draw.text((r_x1, r_y1), txt, font=font, fill=(0,255,0))

plt.imshow(pil)
plt.show()
