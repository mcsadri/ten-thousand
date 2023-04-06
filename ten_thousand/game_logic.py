import random
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(n):
        """
        roll 6 standard 6 sided dice, and return 6 values in between 1 - 6.
        :param n: dice rolled
        :return: a tuple of n numbers/ints each in between 1 - 6, like a standard 6 sided dice
        """
        return tuple(random.randint(1, 6) for _ in range(n))

    # def calculate_score(roll):
    """
    :param roll:
    :return:
    """

    @staticmethod
    def calculate_score(roll):

        score = 0
        count_pair = 0
        count = Counter(roll).most_common()
        num = len(count)
        for num in range(0, len(count)):
            #  ones
            if count[num][0] == 1 and count[num][1] <= 2:
                score += 100 * count[num][1]

            if count[num][0] == 1 and count[num][1] >= 4:
                score += 1000 * (count[num][1] - 2)

            if count[num][0] == 1 and count[num][1] == 3:
                score += 1000

            # twos
            if count[num][0] == 2 and count[num][1] >= 3:
                score += 200 * (count[num][1] - 2)

             # threes
            if count[num][0] == 3 and count[num][1] >= 3:
                score += 300 * (count[num][1] - 2)

            # fours
            if count[num][0] == 4 and count[num][1] >= 3:
                score += 400 * (count[num][1] - 2)

            # fives
            if count[num][0] == 5 and count[num][1] <= 2:
                score += 50 * count[num][1]

            # Add condition for three fives
            if count[num][0] == 5 and count[num][1] == 3:
               score += 500

            if count[num][0] == 5 and count[num][1] > 3:
                score += 500 * (count[num][1] - 2)

            # sixes
            if count[num][0] == 6 and count[num][1] >= 3:
                score += 600 * (count[num][1] - 2)

            # three pair
            if len(count) == 3:
                if count[0][1] == 2 and count[1][1] == 2 and count[2][1] == 2:
                    score = 1500

            # straight
            if len(count) == 6:
                score = 1500

        return score


if __name__ == "__main__":
    print(GameLogic.roll_dice(6))