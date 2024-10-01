# Blackjack Game

## Overview

This project is a simplified version of the classic **Blackjack** game, also known as 21. The game is played between a **player** and the **dealer** (the computer), with the objective being to have cards with a total value closer to 21 than the dealer's cards, without exceeding 21. The game uses a standard deck of cards, with an Ace counting as either 1 or 11 based on the player's choice.

## Rules of the Game

1. The player is dealt two cards initially.
2. The dealer is also dealt two cards, but only one of the dealer's cards is visible to the player.
3. The player can choose to **Hit** (draw another card) or **Stand** (end their turn).
4. The goal is to get the card total as close to 21 as possible without exceeding it.
5. Number cards (2-10) are worth their face value.
6. Face cards (Jack, Queen, King) are worth 10 points.
7. Aces can be worth either 1 or 11, depending on the player's decision.
8. The dealer must hit until their total is 17 or higher.

### Win Conditions

- **Player wins** if their total is closer to 21 than the dealer's without exceeding 21.
- **Dealer wins** if the dealer's total is closer to 21 or if the player goes over 21 (busts).
- **Draw** if both the player and dealer have the same score.

## How to Play

1. The player is asked to choose how they want to count an Ace (1 or 11).
2. The dealer's first card is visible while the second one remains hidden until the player decides to **Stand**.
3. The player can **Hit** to draw another card or **Stand** to stop drawing and let the dealer play.
4. After the player stands, the dealer will reveal their hidden card and draw cards until their score is at least 17.
5. The game compares the final scores to determine the winner.

## Features

- **Randomized Card Dealing**: The cards are shuffled and dealt randomly from a virtual deck.
- **Ace Handling**: Aces can be counted as 1 or 11, based on the player's decision.
- **Automatic Dealer Logic**: The dealer draws cards automatically until the total score is at least 17.
- **Dynamic Win Conditions**: The game checks after each round to see if the player or dealer has won or busted.

## Code Breakdown

### `initial_player_cards()`
This function deals two initial cards to the player and calculates their score based on the card values.

### `initial_computer_cards()`
This function deals two initial cards to the dealer, but only one is visible to the player. The score of the visible card is displayed.

### `update_player_score(card)`
Updates the player’s score after drawing a card. If the card is an Ace, the player decides if it counts as 1 or 11.

### `update_computer_score(card)`
Updates the dealer's score. If the dealer is dealt an Ace, it counts as 11 unless the score would exceed 21, in which case it counts as 1.

### `hit_player_cards()`
Allows the player to draw a new card and updates their score accordingly.

### `hit_computer_cards()`
Allows the dealer to draw cards and updates the score until the dealer reaches at least 17 points.

## Installation and Running

1. **Clone the Repository**:
```bash
git clone https://github.com/lavneethora/Number_Guessing.git
```

2. **Navigate to the Project Directory**:
```bash
cd Number_Guessing
```

3. **Run the Game**:
```bash
python number_guess.py
```

## Sample Game Output

```bash
Welcome to Blackjack!

HOUSE RULES

The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
The computer is the dealer.

Player's cards: ['2', '9']
Player's score: 11

Computer's cards: ['5', 'X']
Computer's score: 5 + ?

Type 'y' to hit, and 'n' to stand: y
New card: Q
Player's cards: ['2', '9', 'Q']
Player's score: 21

Type 'y' to hit, and 'n' to stand: n
Player's cards: ['2', '9', 'Q']
Player's score: 21
Computer's cards: ['5', '3', '2']
Computer's score: 10
Computer busts! Player wins.
```

## Future Improvements

- **Splitting Pairs**: Add functionality to split pairs into two hands.
- **Betting System**: Implement a simple betting system with chips.
- **Multiple Players**: Extend the game to support multiple players in a single round.
- **Graphical Interface**: Create a graphical user interface (GUI) to make the game more interactive.


## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
- Feel free to submit issues or pull requests for any improvements or bug fixes.

## Author

- Lavneet Hora
- Sophomore @ Texas Tech University
- Computer Science
