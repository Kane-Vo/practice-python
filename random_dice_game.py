"""
Write a dice game script that accepts N number of players and M number of players as input
dice, with the following rules:
1. At the start of the game, each player gets a dice of M units.
2. All players will roll their respective dice at the same time
3. Each player will check the results of their roll of the dice and evaluate as follows:
a. Dice number 6 will be removed from the game and added as points
b. for the player.
c. Dice number 1 will be awarded to the player sitting next to him.
d. For example, the first player will give the dice the number 1 to the second player.
e. Dice numbers 2,3,4 and 5 will still be played by the player.
4. After the evaluation, the player who still has the dice will repeat the 2nd step
until only 1 player remains.
a. Players who have no more dice are considered to have finished playing.
5. The player who has the most points wins.
Make this script using the language you are good at.
"""
import random

def rolling_dice(dice_amount):
  new_dices = []
  for dice in range(dice_amount):
    new_dices.append(random.randint(1, 6))

  return new_dices

def main():
  input_amount_player = int(input('Please input amount of player: '))
  input_amount_dice = int(input('Please input amount of dice: '))
  playing_round = 1
  dict_player = {}
  
  for player in range(input_amount_player):
      dict_player[player] = [0, input_amount_dice, None]

  while playing_round:
    stop_player = 0
    print(f"\nRound {playing_round}\n")

    for player in range(input_amount_player):
      print(f"Player {player + 1} ({dict_player[player][0]}): {dict_player[player][2]}")

    print(f"\nAfter evaluate:")

    for player in range(input_amount_player):
      if (dict_player[player][1] == 0):
        dict_player[player][2] = []
        stop_player += 1
        continue

      player_dices = rolling_dice(dict_player[player][1])
      dict_player[player][2] = player_dices

      if (6 in player_dices):
        dict_player[player][0] += 1
        dict_player[player][1] -= 1
     
      if (1 in player_dices):
        next_player = 0 if player == input_amount_player - 1 else player + 1
        dict_player[player][1] -= 1
        dict_player[next_player][1] += 1
      
      print(f"Player {player + 1} ({dict_player[player][0]}): {player_dices}")

    if (stop_player == input_amount_player - 1):
      playing_round = 0
    else:
      playing_round += 1
    print("==============================")
  
  print("\n\n==============RESUTL==============\n")
  winner = 0
  winner_score = dict_player[0]

  for player in range(input_amount_player):
    print(f"Player {player + 1} ({dict_player[player][0]}): {dict_player[player][2]}")
    if dict_player[player][0] > winner_score[0]:
      winner_score = dict_player[player]
      winner = player

  print(f"\n\n Winner is player {winner + 1}")

main()