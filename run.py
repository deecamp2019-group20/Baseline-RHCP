import sys

sys.path.insert(0, 'build/Release')

from env import Env as CEnv


class Env(CEnv):
    @property
    def valid_actions(self):
        return [[]]


class CQL:
    def e_greedy_action(self, *args, **kwargs):
        return 0

    def perceive(self, *args, **kwargs):
        pass


def ai_play():
    env = Env(debug=True)
    lord = CQL()
    lord_win, farmer_win = 0, 0
    for episode in range(3000):
        print('begin')
        env.reset()
        env.prepare()
        r = 0
        while r == 0:  # r == -1 地主赢， r == 1，农民赢
            # lord first
            state = env.face
            action = lord.e_greedy_action(state, env.valid_actions)  # 获取AI的动作
            _, r, _ = env.step(True, action)
            if r == -1:  # 地主赢
                reward = 100
            else:
                _, r, _ = env.step_auto()  # 下家
                if r == 0:
                    _, r, _ = env.step_auto()  # 上家
                if r == 0:
                    reward = 0
                else:  # r == 1，地主输
                    reward = -100
            done = (r != 0)
            lord.perceive(state, action, reward, env.face, done)  # 对AI的reward反馈
            if done:
                break


def 自娱自乐():  # 地主胜率 50%
    env = CEnv()
    total_lord_win, total_farmer_win = 0, 0
    lord_win, farmer_win = 0, 0
    for episode in range(1, 3000 + 1):  # 把他娘的意大利炮拿来，先打上3000轮
        if episode % 100 == 0:
            print('-----------------------------\n'
                  'Lord win rate: \n'
                  '\tRecent 100：{:.2%}\n'
                  '\tTotal {}: {:.2%}\n\n'
                  .format(lord_win / 100, episode, total_lord_win / episode))
            lord_win, farmer_win = 0, 0
        env.reset()
        env.prepare()
        r = 0
        while r == 0:  # r == -1 地主赢， r == 1，农民赢
            # lord first
            _, r, _ = env.step_auto()
            if r == -1:  # 地主赢
                lord_win += 1
                total_lord_win += 1
            else:
                _, r, _ = env.step_auto()  # 下家
                if r == 0:
                    _, r, _ = env.step_auto()  # 上家
                if r == 1:  # 地主输
                    farmer_win += 1
                    total_farmer_win += 1


if __name__ == '__main__':
    自娱自乐()
