# opencv 無法製作透明文字, 用 Pillow 製作
import cv2
import pylab as plt
from PIL import ImageDraw, ImageFont
from PIL import Image
from sdk.IvanCv import IvanCv as cv

img_path = 'E:\project\data\img\yolo7testimg\\0000010.jpg'
txt = 'Coron\n菲律賓科隆島\n日期 : 2023/01/31'
font = ImageFont.truetype('simsun.ttc', 36)

img = cv.read(img_path)
img = cv.resize(img, scale=0.2)
img = img[:, :, ::-1].copy()
h, w, _ = img.shape

pil = Image.fromarray(img)
pil = pil.convert('RGBA')  # A為透明值, 圖_1

# 偵測文字寫入後, 文字所佔的寬與高, 並非實際寫入
# width_txt, height_txt = ImageDraw.Draw(pil).textsize(txt, font=font)
# print(width_txt, height_txt)
_, _, width_txt, height_txt = ImageDraw.Draw(pil).textbbox(xy=(0,0), text=txt, font=font)
print(width_txt, height_txt)

info = pil.copy()  # 圖_2, 畫半透明矩形
x1 = 0
y1 = h-20-height_txt
x2 = 10+width_txt
y2 = h
ImageDraw.Draw(info).rectangle(
    # 左上x1y1, 右下x2y2, (0,0)為左上角, (w, h)為右下角
    # (10, 10, 200, 200),
    # (10, h-10-height_txt, 10+width_txt, h-10),
    (x1, y1, x2, y2),
    fill=(150, 150, 255)
)

# 混合 圖_1 與 圖_2, 各一半透明度, 因此矩形為 0.5透明度
pil = Image.blend(pil, info, 0.5)
# 寫入文字
ImageDraw.Draw(pil).text((x1+10, y1+10), txt, font=font, fill=(255, 255, 255))

plt.imshow(pil)
plt.show()

# 1. 先產生 pil (a圖)，並轉成RGBA
# 2. 由 a 圖複製一張一模一樣的 b 圖
# 3. 在 b 圖畫矩型
# 4. 將 a, b 圖 blend(混圖)，二張圖的 alpha 各為 0.5，加起來為 1
# 5. 將文字寫於 blend後的圖
