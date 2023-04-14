# LAB - Class 08

## Project: Ten Thousand (akd Code Fellows plays Farkle-ish)

## Authors: Manuch Sadri & Deiosha Sparks

### Lab 08 Overview:
- The game should now be close to playable - for honest players at least.
- Let’s shore up the core functionality of game by allowing users to set aside scoring dice and continuing their turn.
- Then we’ll handle cheaters and/or confused players who are skirting the rules.

### Feature Tasks and Requirements

- [X] Application should implement features from versions 1 and 2
- [X] Should handle setting aside scoring dice and continuing turn with remaining dice.
- [X] Should handle when cheating occurs.
  - [X] Or just typos.
  - [X] E.g. roll = `[1,3,5,2]` and user selects `1, 1, 1, 1, 1, 1`
- [X]  Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- [X] Handle **zilch**
  - [X] No points for round, and round is over

### Testing Details

- n/a

### User Acceptance Testing

- [X] Must pass provided unit and simulation tests.

### Stretch Goals

- [ ] Identify features to add and propose idea to client.
- [ ] Identify gaps in current test suite and add tests to expose bugs.

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