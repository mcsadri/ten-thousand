import random
from collections import Counter

"""
pair programming partners: Deiosha Sparks & Manuch Sadri
GameLogic.calculate_score solution with assistance from ChatGPT
"""


class GameLogic:

    @staticmethod
    def roll_dice(n=6):
        """
        roll n qty of standard 6 sided dice, and returns the dice roll values in between 1 - 6.
        :param n: number of dice rolled
        :return: a tuple of n numbers/ints each in between 1 - 6, like a standard 6 sided dice
        """
        if 1 <= n <= 6:
            # using tuple comprehension generate and return n random integers between 1 and 6 (inclusive)
            #return tuple(random.randint(1, 6) for _ in range(n))
            rolled_dice = tuple(random.randint(1, 6) for _ in range(n))
            print(rolled_dice)
            return rolled_dice

        else:
            print("Stop Cheating")
            return "Stop Cheating"

    @staticmethod
    def calculate_score(roll):
        """
        calculate and return the score of the rolled dice from roll_dice()
        :param roll: a tuple containing the results the rolled dice
        :return score: an integer value calculated according to the Ten Thousand scoring rule
        """

        # declare new int variable score = 0
        score = 0
        # declare new int variable count_pair = 0
        count_pair = 0
        # set count = to a list of tuples with the most common values in roll and their respective count
        count = Counter(roll).most_common()
        # declare new int variable = the length of count
        num = len(count)

        # for each in a range of 0 up to the integer length of count
        for num in range(0, len(count)):
            # ones
            # if the count of 1s is <= 2 add 100 * count of 1s to the score
            if count[num][0] == 1 and count[num][1] <= 2:
                score += 100 * count[num][1]
            # if the count of 1s is >= 2 add 1000 * count-2 of 1s to the score
            if count[num][0] == 1 and count[num][1] >= 4:
                score += 1000 * (count[num][1] - 2)
            # if the count of 1s is 3 add 1000 to the score
            if count[num][0] == 1 and count[num][1] == 3:
                score += 1000

            # twos
            # if the count of 2s is >= 3 add 200 * count-2 of 2s to the score
            if count[num][0] == 2 and count[num][1] >= 3:
                score += 200 * (count[num][1] - 2)

            # threes
            # if the count of 3s is >= 3 add 300 * count-2 of 3s to the score
            if count[num][0] == 3 and count[num][1] >= 3:
                score += 300 * (count[num][1] - 2)

            # fours
            # if the count of 4s is >= 3 add 400 * count-2 of 4s to the score
            if count[num][0] == 4 and count[num][1] >= 3:
                score += 400 * (count[num][1] - 2)

            # fives
            # if the count of 5s is <= 2 add 50 * count of 5s to the score
            if count[num][0] == 5 and count[num][1] <= 2:
                score += 50 * count[num][1]
            # if the count of 5s is == 3 add 500 to the score
            if count[num][0] == 5 and count[num][1] == 3:
                score += 500
            # if the count of 5s is > 3 add 500 * count-2 of 5s to the score
            if count[num][0] == 5 and count[num][1] > 3:
                score += 500 * (count[num][1] - 2)

            # sixes
            # if the count of 6s is >= 3 add 600 * count-2 of 6s to the score
            if count[num][0] == 6 and count[num][1] >= 3:
                score += 600 * (count[num][1] - 2)

            # three pair
            # if the length of count == 3 and if the qty value of each tuple in count == 2 set score to 1500
            if len(count) == 3:
                if count[0][1] == 2 and count[1][1] == 2 and count[2][1] == 2:
                    score = 1500

            # straight
            # if the length of count is 6, meaning all possible values 1-6 (inclusive) are present set score to 1500
            if len(count) == 6:
                score = 1500

        # return the value of score
        return score

    @staticmethod
    def play():
        print("Welcome to Ten Thousand")
        count = 0
        score = 0
        dice_qty = 6
        while True and count < 5:
            print("(y)es to play or (n)o to quit")
            player_input = input("> ")
            if player_input == "n" or count == 4 or dice_qty == 0:
                GameLogic.quit(count=count, score=score)
                break
            elif player_input == "y":
                count += 1
                GameLogic.roll_dice(dice_qty)
                print("Enter dice to keep, or (q)uit:")
                banked_dice = input("> ")
                dice_qty -= len(banked_dice)
                scoring_dice = tuple(int(digit) for digit in banked_dice)
                score += GameLogic.calculate_score(scoring_dice)
                print(f"Your total score is {score}")


    @staticmethod
    def quit(score=0, count=0):
        if count == 0:
            print("OK. Maybe another time")
        else:
            print(f"Thanks for playing! You earned {score} points")
        pass


if __name__ == "__main__":
    # declare new variable dice_roll and set it = the results of GameLogic.roll_dice with an int argument of 6
    # dice_roll = GameLogic.roll_dice(7)
    # # print the value of dice_roll to stdout
    # print(dice_roll)
    # # print the returned score value from GameLogic.calculate_score(dice_roll) to stdout
    # print(GameLogic.calculate_score(dice_roll))
    # print(len("Stop Cheating"))

    GameLogic.play()