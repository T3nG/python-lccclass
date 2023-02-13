#訓練模型時, numpy 必需使用 1.21.6
#否則 train.py 的 mode = random.choice(self.sample_options) 會出錯
#但 python 3.8 是安裝 1.24.1
#所以安裝套件的方式如下
#pip install numpy==1.21.6 imgviz labelme pycocotools pyqt5 opencv-python
#pip install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio===0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
#以我們的圖片素材數量，訓練時間約 5.5小時

#weights/resnet50-19c8e357.pth 為空權重, 在此好像沒有什麼用處，但在 train.py 中，會去調用此權重，所以一定要放在
#weights目錄之下

#中斷訓練 : Ctrl+C : 中斷後，會在 weights下產生 yolact_base_xxx_xxx_interrupt.pth
#接續訓練 : python train.py --config=animal_config --resume=weights/yolact_base_xxx_xxx_interrupt.pth

import time
from data import set_cfg
from train import train, args, replace

if __name__=='__main__':
    args.save_folder = 'weights/'
    # 中途有中斷訓練的話，從 xxx.pth 開始訓練
    #args.resume=f'{args.save_folder}/yolact_base_212_424_interrupt.pth'
    args.resume = None
    args.validation_epoch = 2
    args.validation_size = 5000
    args.num_workers = 0  # 依電腦狀況更改
    args.save_interval = 10000
    args.batch_size = 4  # 依電腦狀況更改
    args.log_folder = 'logs/'
    args.cuda = True
    args.log = True
    args.interrupt = True
    args.keep_latest = False
    args.keep_latest_interval = 100000
    args.autoscale = True
    args.dataset = None

    args.lr = None
    args.decay = None
    args.gamma = None
    args.momentum = None

    args.log_gpu = False
    args.batch_alloc = None
    args.start_iter = -1
    args.config='animal_config'
    set_cfg(args.config)

    replace('lr')
    replace('decay')
    replace('gamma')
    replace('momentum')
    replace('momentum')

    t1=time.time()
    print(f'開始訓練 : {t1}....')
    train()
    t2 = time.time()
    seconds=t2-t1
    d=int(seconds//86400)
    h=int(seconds-d*86400)//3600
    m=int((seconds-d*86400-h*3600)//60)
    s=int(seconds-d*86400-h*3600-m*60)
    print(f'總共花費 : {d}天{h:02d}時{m:02d}分{s:02d}秒')