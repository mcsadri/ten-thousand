# LAB - Class 06

## Project: Ten Thousand (akd Code Fellows plays Farkle-ish)
Overview: Create a command line game to play Farkle. Lab 06 will roll dice and calculate score for a single player 
(the user) game. 

## Authors: Manuch Sadri & Deiosha Sparks

### Feature Tasks and Requirements

- Define a `GameLogic` class in `ten_thousand/game_logic.py` file.
- Handle calculating score for dice roll
  - Add calculate_score static method to GameLogic class.
  - The input to `calculate_score` is a tuple of integers that represent a dice roll.
  - The output from `calculate_score` is an integer representing the roll’s score according to rules of game.

- Handle rolling dice
  - Add `roll_dice` static method to GameLogic class.
  - The input to `roll_dice` is an integer between 1 and 6.
  - The output of `roll_dice` is a tuple with random values between 1 and 6.
  - The length of tuple must match the argument given to `roll_dice` method.

- Using the parameters above, use ChatGPT to generate code blocks.
  - You must document every single line of code with a detailed description of what the code is doing.

### Testing Details

- Testing - Roll Dice
  - When rolling 1 to 6 dice ensure…
  - A sequence of correct length is returned
  - Each item in sequence is an integer with value between 1 and 6

- Testing - Calculate Score
*NOTE If there are differences between testing scores and online, the tests will be considered correct.*
  - zilch - roll with no scoring dice should return 0
  - ones - rolls with various number of 1s should return correct score
  - twos - rolls with various number of 2s should return correct score
  - threes - rolls with various number of 3s should return correct score
  - fours - rolls with various number of 4s should return correct score
  - fives - rolls with various number of 5s should return correct score
  - sixes - rolls with various number of 6s should return correct score
  - straight - 1,2,3,4,5,6 should return correct score
  - three_pairs - 3 pairs should return correct score
  - two_trios - 2 sets of 3 should return correct score
  - leftover_ones - 1s not used in set of 3 (or greater) should return correct score
  - leftover_fives - 5s not used in set of 3 (or greater) should return correct score

### Stretch Goals

- Research parametrized tests in PyTest
- Research Behavior Driven Development

---

#### Links and Resources
- back-end server url: n/a
- front-end application: n/a

#### Setup
.env requirements (where applicable)
- i.e.
  - PORT: n/a
  - DATABASE_URL: n/a

#### How to initialize/run your application (where applicable)

- set-up virtual env
  - \> ```python3.11 -m venv .venv```
  - \> ```source .venv/bin/activate```
  - \> ```pip install pytest```
- run cli app
  - \> ```python ten_thousand/game_logic.py```
- run pytest
  - \> ```pytest tests/test_roll_dice```
  - \> ```pytest tests/test_calculate_score```

- deactivate virtual env
  - \> ```deactivate```

#### How to use your library (where applicable)

- Tests
    - How do you run tests?
      - doodah
    - Any tests of note?
      - doodah
    - Describe any tests that you did not complete, skipped, etc
      - doodah