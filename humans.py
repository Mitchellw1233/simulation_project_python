import time
from random import randint
import numpy as np
from Life.human import Human


class Humans:
    def __init__(self, human_count, tests, res):
        self.res = res
        self.humans = []
        self.reproducing_list = []
        self.tests = tests
        self.human_count = human_count
        self.env = [[0] * res for i in range(res)]
        self.start_sim()

    def start_sim(self):
        start = time.time()

        self.env = self.create_env(self.res)

        for x in range(self.human_count):  # 20
            self.humans.append(Human(self.humans, self.env, 0, self.res, self.reproducing_list))
        # print("speed: " + str(self.humans[0].speed))

        end = time.time()
        print(end - start)
        self.run()
        print("Humans alive: " + str(len(self.humans)))

    def run(self):
        for x in range(self.tests):  # 10
            time.sleep(1)
            if self.reproducing_list:
                for h in self.reproducing_list:
                    self.humans.append(h)
                    h.settle()
                self.reproducing_list.clear()

            for human in self.humans:
                if human.walk():
                    print('reproduce')
                    # pass
                    human.reproduce()
                else:
                    print('die')
                    # del human
                    # pass
                    human.die()
            for row in self.env:
                print(' '.join([str(elem) for elem in row]))
            print('\n\n\n')

    @staticmethod
    def create_env(res):
        env = [['0'] * res for i in range(res)]
        # print(len(env))
        for y in range(res):
            for x in range(res):
                item = ['0'] * 80 + ['f'] * 20
                # item[randint(0, len(item) - 1)]
                env[y][x] = item[randint(0, len(item) - 1)]
        return env

        # for row in env:
        #     print(' '.join([str(elem) for elem in row]))

        # for row in env:
        # print('\nits: ' + str(env[99][0]))
        # print("its: " + str(self.get_2d_pos(env, 1, 100)))
        # print(env)
        # print(self.humans)

    def get_2d_pos(self, array, x, y):
        return array[y-1][x-1]


Humans(1, 6, 10)
