# coco只是一個專案代號, 沒特別的意思, 是官網幫我們準備好需要訓練的圖片
'''
train: http://images.cocodataset.org/zips/train2017.zip
test: http://images.cocodataset.org/zips/test2017.zip
validate: http://images.cocodataset.org/zips/val2017.zip
labels: https://github.com/WongKinYiu/yolov7/releases/download/v0.1/coco2017labels-segments.zip

coco2017labels-segments.zip 將其中的 coco解壓縮至專案下
    刪除 coco/images/train2017
        coco/images/val2017
train2017.zip, val2017.zip, test2017.zip 解壓縮至 coco/images
coco/images/將所有類別的圖片, 集合在一個目錄之下
coco/labels/train2017.txt 記錄所有圖片包含的種類(數字), 及標籤種類的座標(均一化)
data/coco.yaml 紀錄 number of classes nc:80種 及 每個種類的名稱 class names(英文)
hyp.scratch.p5.yaml ?
並記錄圖片的路徑

開始訓練
1. 進入命令提示字元
    進入專案底下
    cd E:\GitHub\python-lccclass\20221202_machine_learning\17_yolo7
    venv\Scripts\python train.py --workers 8 --device 0 --batch-size 12 --data data/coco.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --name yolov7 --hyp data/hyp.scratch.p5.yaml --weights ''

    若出錯(BUG), 則
    venv\Scripts\pip install setuptools==59.5.0

    第一次讀取是讀取到 cache裡
2.
    --workders 8
        動用的 CPU數, python只能啟動一顆 CPU, 包含連 i++都無法執行, 如何在訓練時啟動 8顆?
        因為是調用 C語言
    --device 0
        GPU 0
    --batch-size
        12G可調 8, 少於 12G只能調 4, 4G無法執行(COLAB也是 4G)
        20G以上可以調 10左右
    --data data/coco.yaml
        種類檔案及訓練資料
    --cfg cfg/training/yolov7.yaml
        捲積層的設定
    --weights ''
        表示重新開始訓練
    --epochs
        要訓練的次數, 愈多愈準確, 預設 300次, 要約 300小時
3.
    訓練時, 須注意顯卡溫度(可能高達80度), 記得用風扇吹
    400w *0.8 =320瓦, 要花費電費 720左右

訓練時若有發生
    If this all came from a _pb2.py file, your generated code is out if date and must be regenerated with protoc >= 3.19.0
    請使用以下指令將 protobuf 降到 3.20.1版本
    pip3 install --upgrade protobuf==3.20.1

若更改圖片 -- 很重要
    因為訓練時, 會先製作 cache檔, 所以若有更新圖片, 要先砍掉 coco\train2017.cache 及 val2017.cache
    下次訓練時, 才會產生新的 cache檔
監控
    0. 開一個新的命令提示字元
    1. 系統級安裝 pip install tensorboard (儀錶板)
    2. 進入專案下 tensorboard --logdir runs/train
    3. 開啟瀏覽器 localhost:6006

輸出
    訓練好的權重, 儲存在 runs/train/yolov7/weights 目錄之下, 最後的結果是 best.pt
    若中途中斷或手動中斷(ctrl+c), 會產生 last.pt, 可由此處繼續

繼續訓練
    venv\Scripts\python train.py --workers 8 --device 0 --batch-size 8 --data data/coco.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --name yolov7 --hyp data/hyp.scratch.p5.yaml --weights runs/train/yolov7/weights/last.pt
    上述的 weights不可以加 '' => --weights 'runs/train/yolov7/weights/last.pt'

訓練好的模型下載
    http://mahaljsp.asuscomm.com/files/yolov7/coco_best.pt
    下載好後放置專案底下

圖片偵測
    Thomas的模型
    venv\Scripts\python detect.py --weights coco_best.pt --conf 0.3 --source E:\project\data\img\yolo7testimg\f.jpg


'''
