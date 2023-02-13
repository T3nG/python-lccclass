import time
from data import set_cfg
from train import train, args
args.save_folder = 'weights/'
# 若中途有中斷訓練, 從此處xxx.pth開始繼續訓練 , 依最後產生的檔案名稱修改底下程式碼
# args.resume = f'{args.save_folder}/yolact_base_139_278_interrupt.pth'
args.resume = None

args.validation_epoch = 2
args.validation_size = 5000
args.num_workers = 4
args.save_interval = 10000
args.batch_size = 4
args.log = True
args.log_folder = 'logs'
args.cuda = True
args.interrupt = True
args.keep_lastest = None
args.keep_lastest_interval = 100000
args.autoscale = True
args.gamma = None
args.dataset = None
args.log_gpu = False
args.batch_alloc = None
args.start_iter = -1
# args.lr = None
# args.decay = None
# args.momentum = None
replace('lr')
replace('')
replace('')


if __name__ == '__main__':
    args.config = 'animal_config'


    set_cfg(args.config)
    t1 = time.time()
    print(f'開始訓練 : {t1}...')
    train()
    t2 = time.time()
    seconds = t2 - t1
    d = int(seconds//86400)
    h = int(seconds-d*86400)//3600
    m = int((seconds-d*86400-h*3600)//60)
    s = int(seconds-d*86400-h*3600-m*60)
    print(f'總花費時間: {d}天{h:02d}時{m:02d}分{s:02d}秒')