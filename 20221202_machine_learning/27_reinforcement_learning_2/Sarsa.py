from Brain import Brain
class Sarsa(Brain):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super().__init__(actions, learning_rate, reward_decay, e_greedy)

    def q_value(self, s, action, reward, s_next, action_next):
        self.check_state_exist(s_next)
        predict = self.table.loc[s, action]
        if s_next != 'terminal':
            target = reward + self.reward_decay * self.table.loc[s_next, action_next]
        else:
            target = reward
        self.table.loc[s, action] += self.learning_rate * (target - predict)


