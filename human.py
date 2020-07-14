from random import randint
import datetime
import uuid


class Human:

    def __init__(self, humans, env, race, res, reproducing_list):
        self.humans = humans
        self.reproducing_list = reproducing_list
        self.env = env
        self.id = str(uuid.uuid4())  # str(uuid.uuid4()) or 'h'
        self.unique_id = str(uuid.uuid4())
        self.res = res
        self.pos = [randint(0, res-1), randint(0, res-1)]  # [randint(0, 50), randint(90, 99)]
        self.races = ['blue', 'red', 'white']
        self.race = [0] * 90 + [1] * 8 + [2] * 2
        self.race = self.race[randint(0, len(self.race) - 1)]
        race = self.race_func(race)
        self.race = race if race > 0 else self.race

        self.speed = self.speed_func()

        self.food = False
        self.starve_days = 0
        self.max_starve_days = 1  # self.max_starve_days_func()

        self.age = 0  # in artificial days

    def race_func(self, race):
        if race:
            chance = [race] * 95 + [self.race] * 5
            return chance[randint(0, len(chance) - 1)]
        else:
            return 0

    def speed_func(self):
        x = self.race
        return round(((10 - x) * 0.2) / (x+1))

    def max_starve_days_func(self):
        x = self.race
        return round(((6 - self.race) * 0.2) + (self.race - 0.7))

    def settle(self):
        self.food = (self.get_pos(self.env, self.pos[0], self.pos[1]) == 'f')
        self.env[self.pos[1]][self.pos[0]] = self.id

    def walk(self):
        if self.food:
            self.food = False
            return True
        else:
            index_x = []
            index_y = []
            for x in range(1, self.speed + 1):
                if self.pos[0] - x > -1:
                    index_x.append(self.pos[0] - x)
                # index_x.append(self.pos[0] - x)
                if self.pos[0] + x < 100:
                    index_x.append(self.pos[0] + x)

                if self.pos[1] - x > -1:
                    index_y.append(self.pos[1] - x)
                # index_y.append(self.pos[1] - x)
                if self.pos[1] + x < 100:
                    index_y.append(self.pos[1] + x)
                # index_y.append(self.pos[1] + x)
            env_range_x = []
            env_range_y = []
            print('indexes: \n')
            print(index_x)
            print(index_y)
            for i in range(len(index_x)):
                indexx = index_x[i]
                env_range_x.append(self.env[self.pos[1]][indexx])
            for j in range(len(index_y)):
                indexy = index_y[j]
                env_range_y.append(self.env[indexy][self.pos[0]])
            # env_range_x = self.env[self.pos[1]][index_x]
            # env_range_y = self.env[index_y][self.pos[0]]
            print('\nenv_range: \n')
            print(env_range_x)
            print(env_range_y)
            for p in range(len(env_range_x)-1):
                if env_range_x[p] == 'f':
                    self.pos = [index_x[p], self.pos[1]]
                    self.env[self.pos[1]][self.pos[0]] = self.id
                    return True
            for a in range(len(env_range_y)-1):
                if env_range_y[a] == 'f':
                    self.pos = [self.pos[0], index_y[a]]
                    self.env[self.pos[1]][self.pos[0]] = self.id
                    return True

            self.starve_days += 1
            return self.starve_days != self.max_starve_days

    def reproduce(self):
        self.reproducing_list.append(Human(self.humans, self.env, self.race, self.res, self.reproducing_list))
        self.reproducing_list[len(self.reproducing_list)-1].pos = self.pos

    def die(self):  # Je moet ook nog h verwijderen uit env, maar er kan nog een andere human op zelfde plek zitten
        # Daarom is het verstandig om dit over te zetten naar Unity of bouw het wat minder in human class en meer in
        # humans class
        for i in range(len(self.humans) - 1):
            if self.humans[i].unique_id == self.unique_id:
                del self.humans[i]

    def get_pos(self, array, x, y):
        return array[y-1][x-1]
