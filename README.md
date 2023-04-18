# LAB - Class 09

## Project: Ten Thousand (akd Code Fellows plays Farkle-ish)

## Authors: Manuch Sadri & Deiosha Sparks

### Overview:
- Continue work on command line version of the dice game `Ten Thousand` by adding an AI bot to play the game.

### Feature Tasks and Requirements

- Create an AI Bot to play Ten Thousand
  - The only method available for use from Game class is `play`.
  - All static methods of `GameLogic` class are available.
  - All other interactions with game can take place ONLY via the I/O features of the game.
    - In other words, via injectable `print` and `input` functionality.
    - It is FORBIDDEN to inject a custom `roller` function into Game class.

- Copy bots.py to your project.
  - Place it at root of project, at same level as `requirements.txt`

- Your Bot class should be added to `bots.py` file with name of your choosing replacing `YourBot`.
  - NOTE the code for `BaseBot` class is supplied for reference, but your custom code will be in the overridden `_roll_bank_or_quit` and/or `_enter_dice` methods.

- User should be able to see your bot play by executing bots.py from terminal.
- Application should implement all features from previous classes 

- The goal is to beat Nervous Nellie - A reference bot that banks on the first roll every time.

### Testing Details

- n/a

### User Acceptance Testing

- n/a

### Stretch Goals

- [ ] Complete a whiteboard style step through of at least one of the sim files that includes dice rolling (your choice) and test_sims.py
- [ ] Design the best performing bot! We'll showcase the bots on the start of class Tuesday, every team will have the opportunity to share their screen and show their bots running. Highest average score after 100,000 rounds wins. Winner take all

---

### Planning

- n/a

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
- activate virtual env
  - \> ```source .venv/bin/activate```
- install pytest
  - \> ```pip install pytest```
- run cli app
  - \> ```python ten_thousand/game_logic.py```
- run pytest
  - \> ```pytest```
    - \> ```pytest tests/test_roll_dice```
    - \> ```pytest tests/test_calculate_score```
- run bots
  - \> ```python bots.py```
- deactivate virtual env
  - \> ```deactivate```

#### How to use your library (where applicable)

- Tests
    - How do you run tests?
      - run pytest from a virtual environment (see `How to initialize/run your application...` above)
    - Any tests of note?
      - n/a
    - Describe any tests that you did not complete, skipped, etc
      - n/a