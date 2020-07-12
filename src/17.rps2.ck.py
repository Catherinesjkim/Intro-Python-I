import random

wins = 0
losses = 0
ties = 0
choices = ['rock', 'paper', 'scissors']

def compare(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'paper' and computer_choice == 'rock') or \
        (player_choice == 'scissors' and computer_choice == 'paper'):
        return 1
    else:
        return -1
    
while True: # or 1
    print(f'Score: {wins} - {losses} - {ties}')
    cmd = input('\nChoose rock/paper/scissors:\n ')
    # AI picks a random choice from rock/paper/scissors
    ai_choice = choices[random.randrange(3)]
    print(f'Computer chose {ai_choice}')
    # comparison function - REPL - will only do one simple task - win, losses, & ties - numerical values 
    results = compare(cmd, ai_choice)
    if results == 1:
        wins += 1
        print('You won!')
    elif results == -1:
        losses +=1
        print("Sorry, you lost!")
    elif results == 0:
        ties += 1
        print("Tie!")
    if cmd == 'quit':
        print('Goodbye')
        break