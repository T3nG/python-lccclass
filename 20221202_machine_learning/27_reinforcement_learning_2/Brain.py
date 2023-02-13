import numpy as np
import pandas as pd


class Brain():
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        # actions => 0: up, 1: down, 2: left, 3: right
        self.actions = actions  # [0,1,2,3]
        self.learning_rate = learning_rate  # lr
        self.reward_decay = reward_decay  # gamma
        self.e_greedy = e_greedy  # epsilon
        self.table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def choose_action(self, s):
        self.check_state_exist(s)
        if np.random.uniform() < self.e_greedy:  # 小於則驗證
            state_action = self.table.loc[s, :]
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:  # 大於則隨機選取上下左右的動作
            action = np.random.choice(self.actions)
        return action

    def check_state_exist(self, s):
        if s not in self.table.index:
            s = pd.Series(
                [0]*len(self.actions),
                index=self.table.columns,
                name=s
            )
            self.table = pd.concat([self.table, pd.DataFrame(s).T])  # T 置轉90度, 直向變橫向
            print('=======新狀態=======')
            print(self.table)

    def q_value(self, s, action, reward, s_next):
        self.check_state_exist(s_next)
        if s_next != 'terminal':
            target = reward + self.reward_decay * self.table.loc[s_next, :].max()
        else:
            target = reward
        self.table.loc[s, action] += self.learning_rate * (target - self.table.loc[s, action])