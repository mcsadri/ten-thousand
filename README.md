# LAB - Class 06

## Project: Ten Thousand (akd Code Fellows plays Farkle-ish)

Overview: Extend Ten Thousand game started in previous class to get the game in playable state.

## Authors: Manuch Sadri & Deiosha Sparks

### Feature Tasks and Requirements

- [X] Application should implement all features from previous version
- [X] Application should allow user to set aside dice each roll
- [X] Application should allow “banking” current score or rolling again.
- [X] Application should keep track of total score
- [X] Application should keep track of current round

### Planning

![GameLogic Planning Flowchart](assets/game_logic_planning_flowchart.jpg)

### Testing Details

- n/a

### User Acceptance Testing

- Starter code contains “simulation” text files.
  - E.g. `tests/version_2/quitter.sim.txt`
- NOTE: Feel free to add more simulations, but you are required to pass all existing ones.
- The simulations are the official documentation of the features for the day.

### Stretch Goals

- [ ] Application should have automated tests to ensure proper operation

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