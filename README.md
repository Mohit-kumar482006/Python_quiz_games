# Python_quiz_games
A command-line quiz game built in Python. The player answers 5 multiple-choice questions across general knowledge and basic computer science topics, and gets a final score at the end.
 

---

## How It Works

1. The game welcomes the player and starts the quiz
2. Each question is displayed with 4 options (a/b/c/d)
3. The player types their answer
4. Instant feedback is given — correct or wrong (with the right answer shown)
5. Final score out of 5 is displayed at the end

---

## Questions Covered

| # | Topic |
|---|---|
| 1 | Capital of France |
| 2 | Language used to build the game |
| 3 | Full form of CPU |
| 4 | The Red Planet |
| 5 | Python data types |

---

## Code Structure

| Part | Description |
|---|---|
| `ask_question()` | Function that displays a question, takes user input, checks the answer, and returns 1 or 0 |
| `score` | Variable that accumulates points across all questions |
| `q1_options` – `q5_options` | Dictionaries holding the answer choices for each question |
| Main block | Calls `ask_question()` five times and prints the final score |

---

## Concepts Used

| Concept | Where Used |
|---|---|
| Functions (`def`) | `ask_question()` to reuse question logic |
| Dictionaries | Storing answer options for each question |
| `for` loop | Iterating over options to display them |
| `input()` | Taking player's answer |
| Conditionals (`if/else`) | Checking correct vs wrong answer |
| Return values | Returning score points from the function |
| String methods (`.lower()`) | Making input case-insensitive |
| `+=` operator | Accumulating the score |

---

## How to Run

Make sure Python is installed, then run:

```bash
python quiz_game.py
```

No external libraries needed — uses only built-in Python.

---

## Sample Output

```
Welcome to Quiz Game!
----------------------

What is the capital of France?
a) Paris
b) London
c) Berlin
d) Rome
Enter your answer (a/b/c/d): a
Correct!

...

Your final score is: 4 / 5
```
