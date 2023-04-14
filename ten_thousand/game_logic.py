import random
from collections import Counter
import re

"""
pair programming partners: Deiosha Sparks & Manuch Sadri
GameLogic.calculate_score solution with assistance from ChatGPT
"""


class GameLogic:

    @staticmethod
    def roll_dice(n=6):
        """
        roll n qty of standard 6 sided dice, and returns the dice roll values in between 1 - 6.
        :param: number of dice rolled
        :return: a tuple of n numbers/ints each in between 1 - 6, like a standard 6 sided dice
        """
        # if 1 <= n <= 6:
            # using tuple comprehension generate and return n random integers between 1 and 6 (inclusive)
            # return tuple(random.randint(1, 6) for _ in range(n))
        rolled_dice = tuple(random.randint(1, 6) for _ in range(n))
        output = "*** " + " ".join(str(i) for i in rolled_dice) + " ***"
        print(output)
        return rolled_dice
        # else:
        #     print("Stop Cheating")
        #     return "Stop Cheating"

    @staticmethod
    def roll_bank_quit(score, dice_qty, total_score, count):
        """
        prompt the player to either roll again, bank the current score, or quit the game
        :param score: (int) holds current roll scoring
        :param dice_qty: (int) holds current qty of dice to be rolled, range 1-6
        :param total_score: (int) holds cumulative game score
        :param count: (int) holds counter value for # of game rounds played
        :return: player_input (string), total_score (int)
        """
        print(f"You have {score} unbanked points and {dice_qty} dice remaining")
        while True:
            print("(r)oll again, (b)ank your points or (q)uit:")
            player_input = (input("> ")).lower()
            if player_input in ["r", "b", "q"]:
                break
        if player_input == "q":
            GameLogic.quit(total_score, count)
        elif player_input == "b":
            print(f"You banked {score} points in round {count}")
            total_score += score
            print(f"Total score is {total_score} points")
        return player_input, total_score

    @staticmethod
    def bank_dice():
        """
        prompt the user to either specify which of the rolled dice they want to keep for scoring, or quit
        :return: banked_dice (string)
        """
        while True:
            pattern = r"^(?:[1-6]{1,6}|q)$"  # regex pattern via assistance from ChatGPT
            print("Enter dice to keep, or (q)uit:")
            banked_dice = (input("> ")).lower()
            if re.match(pattern, banked_dice):
                break
        return banked_dice

    def play_round(total_score, count):
        """
        play one round of the game Ten Thousand
        :param total_score: (int) holds cumulative game score
        :param count: (int) holds counter value for # of game rounds played
        :return: total_score (int), count (int)
        """
        dice_qty = 6
        score = 0
        player_input = str()
        print(f"Starting round {count}")
        while player_input != "b" and player_input != "q":
            print(f"Rolling {dice_qty} dice...")
            rolled_dice = GameLogic.roll_dice(dice_qty)
            if GameLogic.calculate_score(rolled_dice) == 0:
                print("****************************************")
                print("**        Zilch!!! Round over         **")
                print("****************************************")
                break
            banked_dice = GameLogic.bank_dice()
            if banked_dice == "q":
                GameLogic.quit(total_score, count)
            else:
                dice_qty -= len(banked_dice)
                scoring_dice = tuple(int(digit) for digit in banked_dice)
                score += GameLogic.calculate_score(scoring_dice)
                player_input, total_score = GameLogic.roll_bank_quit(score, dice_qty, total_score, count)
        total_score += score
        print(f"You banked {score} points in round {count}")
        print(f"Total score is {total_score} points")
        count += 1
        if dice_qty == 0:
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")
        return total_score, count

    @staticmethod
    def quit(total_score=0, count=0):
        """
        quit the game, and display the player's score if they played one or more rounds
        :param total_score: (int) holds cumulative game score
        :param count: (int) holds counter value for # of game rounds played
        :return: none
        """
        if count == 0:
            print("OK. Maybe another time")
        else:
            print(f"Thanks for playing! You earned {total_score} points")
        exit()

    @staticmethod
    def welcome():
        """
        display a welcome message to the player, and verify they want to play
        :return: none
        """
        player_input = str()
        print("Welcome to Ten Thousand")
        while player_input != "y":
            print("(y)es to play or (n)o to decline")
            player_input = (input("> ")).lower()
            if player_input == "n":
                GameLogic.quit(0, 0)

    @staticmethod
    def play_game():
        """
        manages the Ten Thousand game, tracks cumulative score, round #, and limits game to 20 maximum rounds
        :return: none
        """
        count = 1
        total_score = 0
        has_played = False  # added variable to keep track of whether the player has already entered "y"
        while True and count <= 20:
            if not has_played:  # check if the player has already entered "y"
                GameLogic.welcome()
                has_played = True  # set the variable to True
            total_score, count = GameLogic.play_round(total_score, count)
        GameLogic.quit(total_score, count - 1)

    @staticmethod
    def calculate_score(roll):
        """
        calculate and return the score of the rolled dice from roll_dice()
        :param: roll: a tuple containing the results the rolled dice
        :return: score: an integer value calculated according to the Ten Thousand scoring rule
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


if __name__ == "__main__":
    GameLogic.play_game()