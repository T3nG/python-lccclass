# pip install pandas
# ref: https://mofanpy.com/tutorials/machine-learning/reinforcement-learning/general-rl
# ref: http://mahaljsp.asuscomm.com/index.php/2023/01/04/q-learning-maze/
# 二維的走法
import pandas as pd

from Brain import Brain
from Maze import Maze
from Sarsa import Sarsa

epochs = 100


def sarsa_update():
    for epoch in range(epochs):
        s = maze.reset()
        while True:
            action = ag.choose_action(str(s))
            # 決定下一個狀態, 回報值, 是否終止
            s_next, reward, done = maze.step(action)
            action_next = ag.choose_action(str(s_next))
            # 依 reward計算 s狀態下每個動作的 Q值
            ag.q_value(str(s), action, reward, str(s_next), action_next)
            s = s_next
            maze.render()  # 才看得到紅色矩形在移動
            if done:
                break
        print(f'epoch: {epoch}')
    print('=======final table=======')
    df = pd.DataFrame({
        'up': ag.table[0],
        'down': ag.table[1],
        'left': ag.table[2],
        'right': ag.table[3],
        'max': ag.table.max(axis=1)
        },
        index=ag.table.index
    )
    print(df.applymap(lambda x: '%.5f' % x))


def brain_update():
    for epoch in range(epochs):
        s = maze.reset()
        while True:
            action = ag.choose_action(str(s))
            # 決定下一個狀態, 回報值, 是否終止
            s_next, reward, done = maze.step(action)
            # 依 reward計算 s狀態下每個動作的 Q值
            ag.q_value(str(s), action, reward, str(s_next))
            s = s_next
            maze.render()  # 才看得到紅色矩形在移動
            if done:
                break
        print(f'epoch: {epoch}')
    print('=======final table=======')
    df = pd.DataFrame({
        'up': ag.table[0],
        'down': ag.table[1],
        'left': ag.table[2],
        'right': ag.table[3],
        'max': ag.table.max(axis=1)
        },
        index=ag.table.index
    )
    print(df.applymap(lambda x: '%.5f' % x))


if __name__ == '__main__':
    maze = Maze()
    maze.geometry('+1000+500')

    # Q-Learning
    # ag = Brain(actions=list(range(4)))
    # maze.after(100, brain_update)

    # Sarsa
    ag = Sarsa(actions=list(range(4)))
    maze.after(100, sarsa_update)  # 延遲 100ms後執行 update()

    maze.mainloop()


# 這個 Q Table即是訓練的成果
# 當狀態達到千種, 動作達萬種時, Q Table 會非常大
# 除了記憶體不夠用外, 還會花很長的時間進行搜尋
# 所以必須使用 Deep Q Network (DQN)

# Q Learning: 折扣因子 * maxQ(s'), max為最大值, 是一種決策
# 若把 max拿掉, 此種演算法稱為 Sarsa

'''Q Learning
x, y = 
    0,0  1,0  2,0  3,0
    0,1  1,1  2,1  3,1
    0,2  1,2  2,2  3,2
    0,3  1,3  2,3  3,3
    
                up      down      left     right      max
(0, 0)     0.00000   0.00015   0.00000   0.00000  0.00015
(0, 1)     0.00000   0.00123   0.00000   0.00000  0.00123
(1, 1)     0.00000  -0.01990   0.00000  -0.01000  0.00000
terminal   0.00000   0.00000   0.00000   0.00000  0.00000
(1, 0)     0.00000   0.00000   0.00000   0.00000  0.00000
(0, 2)     0.00000   0.00825   0.00006  -0.01990  0.00825
(0, 3)     0.00001   0.00014   0.00044   0.04589  0.04589
(1, 3)    -0.03940   0.00114   0.00039   0.19031  0.19031
(2, 3)     0.57441   0.00481   0.00085   0.00000  0.57441
(2, 0)     0.00000  -0.01990   0.00000   0.00000  0.00000
(3, 0)     0.00000   0.00000   0.00000   0.00000  0.00000
(3, 1)     0.00000   0.00018  -0.01000   0.00000  0.00018
(3, 2)     0.00000   0.00000   0.02970   0.00018  0.02970
(3, 3)     0.00009   0.00000   0.00000   0.00000  0.00009
'''


'''Sarsa
                up      down      left     right       max
(0, 0)    -0.00001  -0.00001  -0.00001  -0.00003  -0.00001
(1, 0)    -0.00001  -0.00059  -0.00001  -0.00028  -0.00001
(1, 1)    -0.00000  -0.01990  -0.00000  -0.04901  -0.00000
(0, 1)    -0.00001  -0.00028  -0.00001  -0.00007  -0.00001
terminal   0.00000   0.00000   0.00000   0.00000   0.00000
(0, 2)     0.00000   0.00092  -0.00009  -0.04901   0.00092
(0, 3)     0.00000   0.00000   0.00001   0.00965   0.00965
(1, 3)    -0.01000   0.00000   0.00008   0.06934   0.06934
(2, 0)    -0.00009  -0.01990  -0.00000   0.00019   0.00019
(2, 3)     0.36381   0.00000   0.00077   0.00001   0.36381
(3, 0)     0.00005   0.00299   0.00000   0.00000   0.00299
(3, 1)     0.00001   0.03971  -0.03940   0.00000   0.03971
(3, 2)     0.00000   0.00000   0.30359   0.00286   0.30359
(3, 3)     0.00360   0.00000   0.00000   0.00000   0.00360
'''