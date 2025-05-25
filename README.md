### Hexlet tests and linter status:
[![Actions Status](https://github.com/Surtral/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Surtral/python-project-49/actions)


### Asciinema
python-project-49/brain-calc.cast
python-project-49/brain-games.cast
python-project-49/brain-gcd-cast
python-project-49/brain-prog.cast
python-project-49/brain-prime.cast

# Hexlet Code

Welcome to the Hexlet Code project! This repository contains a series of interactive brain games implemented in Python.

## Description

This project is a collection of small brain games that are played via the command line. Each game poses a series of questions and the player must provide the correct answers to win. 

Games include:

- **Brain Games**: Answer the given questions correctly to win.
- **Brain Even**: Determine if the given number is even.
- **Brain Calc**: Calculate the result of simple arithmetic expressions.
- **Brain GCD**: Find the greatest common divisor of given numbers.
- **Brain Prime**: Determine if the given number is prime.
- **Brain Progression**: Find the missing number in a sequence progression.


## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd python-project-49
   ```

2. Install the dependencies:

   ```bash
   make install
   ```

3. Install the package:

   ```bash
   make package-install
   ```

## Usage

After installation, you can play the games using the provided commands:

- **Brain Games**:

  ```bash
  brain-games
  ```

- For individual games, use:

  ```bash
  brain-even
  brain-calc
  brain-gcd
  brain-prime
  brain-progression
  ```

Each command will launch its respective game in the terminal, where you can follow the on-screen instructions to play.

## Development

To contribute or make modifications, follow these steps:

1. Run the development server:

   ```bash
   uv run <command>  # Replace <command> with the game you want to develop or test
   ```

2. Lint and auto-fix code style issues:

   ```bash
   make lint
   ```

3. Run tests:

   ```bash
   pytest
   ```
