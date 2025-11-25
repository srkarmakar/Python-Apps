import random

def get_choices():
    player_choice = input('Please type your choice (rock, paper, scissors):')
    options = ['rock', 'paper','scissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices

def decisions(player, computer):
    print(f"You chose {player} & Computer chose {computer}")

    if player == computer:
        print(f"It's a Tie...")
    elif player == 'rock':
        if computer == 'paper':
            print(f'Computer Wins !')
        else: 
            print(f"You Win !")
    elif player == 'paper':
        if computer == 'scissors':
            print(f'Computer Wins !')
        else: 
            print(f"You Win !")
    elif player == 'scissors':
        if computer == 'rock':
            print(f'Computer Wins !')
        else: 
            print(f"You Win !")

choices = get_choices()
finale = decisions(choices['player'], choices['computer'])