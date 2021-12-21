import helper
from AOCSolver import AOCSolver
from collections import defaultdict

class AOCSolver_2021_21(AOCSolver):

    def parse(self, input):
        self.table = [int(x.split(": ")[1]) for x in input.strip().split('\n')]
        self.wins = [0, 0]



    def execute(self, part=1):
        pos = helper.copy_table(self.table)
        score = [0, 0]
        roll = 1
        player = 0
        if part == 1:
            while True:
                new_pos = (pos[player] + 2 + 3 * roll) % 10 + 1
                score[player] += new_pos
                roll += 3
                pos[player] = new_pos
                if score[player] >= 1000:
                    return score[1 - player] * (roll - 1)
                player = 1 - player


        poss = {(0, 0, pos[0],pos[1]): 1}
        count = [0 for i in range(10)]
        for v in helper.flatten(helper.flatten([[[i + j + k for i in range(1, 4)] for j in range(1, 4)] for k in range(1, 4)])):
            count[v] += 1

        while bool(poss):
            new_poss = defaultdict(int)
            for state, poss_count in list(poss.items()):
                self.compute_turn(count, poss_count, new_poss, state)
            poss = new_poss
        return max(self.wins)

    def compute_turn(self, count, poss_count, new_poss, state):
        old_score1, old_score2, old_pos1, old_pos2 = state
        for sum_dice in range(3, 10):
            pos1, score1 = self.compute_new_state(old_pos1, old_score1, sum_dice)
            if score1 >= 21:
                self.wins[0] += poss_count * count[sum_dice]
                continue
            for sum_dice2 in range(3, 10):
                pos2, score2 = self.compute_new_state(old_pos2, old_score2, sum_dice2)
                if score2 >= 21:
                    self.wins[1] += poss_count * count[sum_dice] * count[sum_dice2]
                    continue
                new_poss[(score1, score2, pos1, pos2)] += poss_count * count[sum_dice] * count[sum_dice2]

    @staticmethod
    def compute_new_state(old_pos, old_score, sum_dice):
        pos = (old_pos + sum_dice - 1) % 10 + 1
        return pos, old_score + pos