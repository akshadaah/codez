rock = ''' 
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\

'''
paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|           
'''
scissors = '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/

'''
import random
print("Welcome to Rock, Paper, Scissors!")
print(" What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)
    
computer_choice = random.randint(0, 2)
print(f"computer choose {computer_choice}")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)
  
if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif user_choice == 1 and computer_choice == 0:
  print("You win!")
elif user_choice == 2 and computer_choice == 1:
  print("You win!")
else:
  print("You lose!")
  