# Python Minesweeper 💣

A __Minesweeper__ protoype written in __Python__ using John Zelle's __graphics.py__ (simple object oriented graphics library). This was a small side-project that lasted 2 weeks to apply and practise the skills I learned in the first half of my first teaching block in my first-year Programming module, at the University of Portsmouth.

![Minesweeper Example](./README-images/game-flag.png)

## Table of contents 📖
- [Overview](#overview)
- [Main Features](#main-features)
  - [Start Page](#start-page)
  - [Size & Difficulty](#Different-Game-Sizes-and-Difficulty)
  - [Flagging Mines](#flag-mode)
- [Requirements](#requirements)
- [Usage](#usage)
- [Last Note](#note)

## Overview

The primary objective of this side-project was to develop a working prototype of __Minesweeper__. The prototype needed to have an intuitive user interface and basic features such as flagging bombs, and clearing spaces with no bombs.

## Main Features

### Start Page

A fully interactive and intuitive start page where you can select the difficulty and the map size.

#### Start Page
![Start Page Menu](./README-images/start-page.png)

#### Chosen Settings ⚙️
![Chosen Settings](./README-images/start-page-selected.png)

### Working Game 🕹️

Functioning minesweeper, where you can _clear_ and _flag_ spaces, see the _total number of mines_, and the _number of flags placed_.

#### Blank Game
![Blank Game](./README-images/blank-game.png)

#### Small Cleared Section
![Sweepen Game](./README-images/game-sweep.png)

### Flag Mode ⛳️
![Flagged Mines](./README-images/game-flag.png)

#### Placing Flags
![Flagged Mines 2](./README-images/game-flag2.png)

#### Cleared Game
![Cleared Game](./README-images/cleared.png)

### Different Game Sizes and Difficulty

Functioning game size settings with a set size of __easy__: 10 x 10, __medium__: 20 x 20 and __hard__: 30 x 30. The different difficulty settings were determined by the chance of a space having a mine, __easy__: 15%, __medium__: 20% and __hard__: 25%.

#### Difficulty: Easy, Size: Large
![Easy Difficulty Large Map](./README-images/easy-large.png)

#### Difficulty: Hard, Size: Medium
![Hard Difficulty Medium Map](./README-images/hard-medium.png)

#### Difficulty: Medium, Size: Small
![medium Difficulty Small Map](./README-images/medium-small.png)


## Requirements

* Python 3
* graphics.py

This project utilises John Zelle's __graphics.py__ library. Please ensure this is in the same directory as the __mineSweeper.py__ for the Minesweeper to function properly.

## Usage

1. Clone this project
2. Run [__mineSweeper.py__](./mineSweeper.py)
3. Choose your difficulty and size

### Note

This is project is still __unfinished__ with some features still missing such as, a win window, a way of keeping track of previous attempts, etc.

## Thank you for reading 👋
