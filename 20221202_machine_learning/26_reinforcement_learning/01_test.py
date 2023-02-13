# pip install pandas
# ref: https://mofanpy.com/tutorials/machine-learning/reinforcement-learning/general-rl
# ref: http://mahaljsp.asuscomm.com/index.php/2023/01/03/q-learning/
# 一維的走法
import numpy as np
import pandas as pd
import time

np.random.seed(1)
status = 6  # 6種狀態
actions = ['left', 'right']  # 2種動作

# 狀態: [貧窮, 小康, 富有]
# 動作: [買房, 買車, 買吃]
# 現實世界中, 並不是每一種狀態都有相同的動作
# 初學時, 必須把問題簡化, 再慢慢地複雜化

epsilon = 0.9  # 貪婪程度: 少於 0.9就亂數隨便選擇動作, 0.9以上就驗證
lr = 0.1  # 學習率
gamma = 0.9  # 折扣因子
epochs = 40  # 世代
delay = 0.1 #  每個 epoch 延遲個 0.1秒

def build_table(status, actions):
    table = pd.DataFrame(
        np.zeros((status, len(actions))),
        columns=actions
    )
    return table

def show(s, e, step_counter):
    env_list = ['-']*(status-1)+['T']  # -----T
    if s == 'terminal':
        print(f'\nEpoch {e+1}: total steps={step_counter}')
        time.sleep(delay)
        print('\r', end='')
    else:
        env_list[s] = 'o'
        interaction = ''.join(env_list)  # 將 list變成字串  o----T
        print(f'\r{interaction}', end='')  # 同位置變化, 不換行, \r 由最前面開始列印
        time.sleep(delay)

def choose_action(s, table):
    state_action = table.iloc[s, :]
    if np.random.uniform() > epsilon or (state_action == 0).all():
        action_name = np.random.choice(actions)
    else:  # 貪婪模式
        action_name = state_action.idxmax()
    return action_name

def get_reward(s, a):
    if a == 'right':  # 若往右
        if s == status - 2:  # 終點前一站
            s_next = 'terminal'
            reward = 1
        else:
            s_next = s + 1
            reward = 0
    else:  # 若往左
        reward = 0
        if s == 0:
            s_next = s
        else:
            s_next = s-1
    return s_next, reward

def rl():
    table = build_table(status, actions)  # 建立一個空的 Q Table
    for e in range(epochs):
        step_counter = 0
        s = 0  # 一開始位於最初狀態(最左)
        runFlag = True  # 直到 s = 5(最右) 才變 False
        show(s, e, step_counter)
        while runFlag:  # 計算每一個狀態的 Q值
            a = choose_action(s, table)  # 取得要做什麼動作
            s_next, reward = get_reward(s, a)
            # 計算 lr 後面的值 r+gamma*maxQ(s')
            if s_next != 'terminal':
                target = reward + gamma * table.iloc[s_next, :].max()
            else:
                target = 1
                runFlag = False
            # Q-Learning 公式
            table.loc[s, a] = table.loc[s, a] + lr * (target - table.loc[s, a])
            s = s_next
            show(s, e, step_counter+1)
            step_counter += 1
        print('\r')
        print(table.applymap(lambda x: '%.10f' % x))
    return table


if __name__ == '__main__':
    table = rl()  # 由強化學習取得 Q Table
    print('最後的table: ')
    # 匿名函數, 印出小數10後位數
    print(table.applymap(lambda x: '%.10f' % x))

