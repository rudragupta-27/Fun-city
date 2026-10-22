import sys
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# tictactoe
def print_board(board):
    i=0
    for row in board:
        print(" | ".join(row))
        if i< len(board)-1:
            print("---------")
        i+=1
    print()
def make_move(board,row,col,symbol):
    if board[row][col]==" ":
        board[row][col]=symbol
        return True
    return False
def check_win(board,symbol):
    board_array=np.array(board)
    for i in range(3):
        if np.all(board_array[i]==symbol) or np.all(board_array[:,i]==symbol):
            return True
    if np.all(np.diag(board_array)==symbol) or np.all(np.diag(np.fliplr(board_array))==symbol):
        return True
    return False
def check_draw(board):
    return all([cell!=" " for row in board for cell in row])

#rockpaper
def determine_winner(player_choice,computer_choice):
    if player_choice==computer_choice:
        return "tie"
    elif (player_choice=="rock" and computer_choice=="scissors") or \
         (player_choice=="paper" and computer_choice=="rock") or \
         (player_choice=="scissors" and computer_choice=="paper"):
        return "player"
    else:
        return "computer"

# NumberGuezz
class NumberGuezz:
    def __init__(self,lower_bound,upper_bound,max_attempts):
        self.lower_bound=lower_bound
        self.upper_bound=upper_bound
        self.max_attempts=max_attempts
        self.secret_number=random.randint(lower_bound, upper_bound)
        self.attempts=0

    def get_guess(self):
        while True:
            try:
                guess=int(input(f"Guess a number between {self.lower_bound} and {self.upper_bound}: "))
                if self.lower_bound<=guess<=self.upper_bound:
                    return guess
                else:
                    print("Invalid input. Please enter a number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self):
        print("Welcome to the Number Guessing Game!")
        while self.attempts<self.max_attempts:
            guess=self.get_guess()
            self.attempts+=1
            if guess==self.secret_number:
                print(f"Congratulations! You guessed the secret number {self.secret_number} in {self.attempts} attempts.")
                return
            elif guess<self.secret_number:
                print("Nahh")
            else:
                print("Nahh")
        print(f"Sorry, you ran out of attempts! The secret number was {self.secret_number}.")

# Advanced Number Guezz
class AdvancedNumberGuessGame(NumberGuezz):
    def __init__(self,lower_bound,upper_bound,max_attempts):
        super().__init__(lower_bound,upper_bound,max_attempts)
        self.hints_enabled=True

    def play(self):
        print("Welcome to the Advanced Number Guessing Game!")
        while self.attempts<self.max_attempts:
            guess=self.get_guess()
            self.attempts+=1
            if guess==self.secret_number:
                print(f"Congratulations! You guessed the secret number {self.secret_number} in {self.attempts} attempts.")
                return
            elif guess<self.secret_number:
                print("Too low!")
                if self.hints_enabled:
                    print(f"The secret number is greater than {guess}.")
            else:
                print("Too high!")
                if self.hints_enabled:
                    print(f"The secret number is less than {guess}.")
        print(f"Sorry, you ran out of attempts! The secret number was {self.secret_number}.")

#Splitwise
def members(no):
    i=1
    while no>0:
        name=input(f"Enter Name {i}: ").upper()
        friends[name]=0  
        i+=1
        no-=1
    
def expense(total,no):
    while True:
        try:
            amount=int(input("Enter amount spent: "))
            name=input("Who spent it? ").upper()
            friends[name]=friends.get(name, 0) + amount 
            total+=amount
            choice=input("Do you want to add another expense?(Y/N) ").upper()
            if choice=="N":
                break
            elif choice!="Y":
                print("Invalid Choice.")
        except ValueError:
            print("Invalid input. Please enter a number for the amount.")

    print(friends)
    print(f"Total expense of group is {total}.")
    owe(total,no)
    return total 

def owe(total,no):
    each=total/no
    for i in friends:
        if friends[i]>each:
            print(f"{i} is owed {friends[i]-each} {currency}.")
        elif friends[i]<each:
            print(f"{i} owes {each-friends[i]} {currency}.")
        else:
            print(f"{i} does not owe anything.")

#Quiz
def choose():
    quizes=["Anime Quiz","Python Quiz"]
    for index, option in enumerate(quizes,start=1):
        print(f"{index}: {option}")
    choice=int(input("Enter the number corresponding to your choice: "))
    if choice in [1,2]:
        quiz(choice)
    else:
        print("Invalid choice! Please select a valid option.")
        choose()
    
def quiz(choice):
    right=0
    wrong=0
    if choice==1:
        questions=[
            ("What does 'Kaizoku ou ni ore wa naru' mean in English?", 
             ["A- I will be Hokage!", 
              "B- I will become the Pokemon Master!", 
              "C- I will be the King of Pirate!", 
              "D- I am a Saiyan from Earth."], 
             "C"),
             
            ("Who is Pain's Sensei?", 
             ["A- Jiraya Sensei", 
              "B- King Kai", 
              "C- Koro Sensei", 
              "D- Kakashi Sensei"], 
             "A"),
             
            ("Who is Natsu's father?", 
             ["A- Acnologia", 
              "B- Igneel", 
              "C- Aldoron", 
              "D- Ignia"], 
             "B"),
             
            ("Who is the villain in Demon Slayer?", 
             ["A- Muzan Kibutsuji", 
              "B- Tanjiro Kamado", 
              "C- Michael Jackson", 
              "D- Goku"], 
             "A"),
             
            ("Who is Ash's first Pokemon?", 
             ["A- Pikachu", 
              "B- Charmander", 
              "C- Squirtle", 
              "D- Lugia"], 
             "A")
        ]
        for question, options, correct_answer in questions:
            print(question)
            for option in options:
                print(option)
            ans=input("Enter your choice: ").upper()
            if ans==correct_answer:
                time.sleep(1)
                print("Right Answer!")
                right+=1
            else:
                time.sleep(1)
                print("Sorry! Wrong Answer")
                wrong+=1
        time.sleep(2)
        print(f"\nQuiz Finished! You got {right} right answers and {wrong} wrong answers.")
        
    elif choice==2:
        questions=[
            ("What is the output of print(2 ** 3)?", 
             ["A- 6", 
              "B- 8", 
              "C- 9", 
              "D- 3"], 
             "B"),
             
            ("Which of the following is a mutable data type?", 
             ["A- Tuple", 
              "B- String", 
              "C- List", 
              "D- Dictionary"], 
             "C"),
             
            ("What keyword is used to define a function in Python?", 
             ["A- func", 
              "B- define", 
              "C- def", 
              "D- function"], 
             "C"),
             
            ("What will be the output of 'Hello, World!'[7]?", 
             ["A- H", 
              "B- W", 
              "C- o", 
              "D- ,"], 
             "B"),
             
            ("Which of the following is not a valid variable name in Python?", 
             ["A- my_var", 
              "B- _myVar", 
              "C- myVar1", 
              "D- 1myVar"], 
             "D")
        ]                
        for question, options, correct_answer in questions:
            print(question)
            for option in options:
                print(option)
            ans=input("Enter your choice: ").upper()
            if ans==correct_answer:
                time.sleep(1)
                print("Right Answer!")
                right+=1
            else:
                time.sleep(1)
                print("Sorry! Wrong Answer")
                wrong+=1
        time.sleep(2)
        print(f"\nQuiz Finished! You got {right} right answers and {wrong} wrong answers.")

#Main       
print("\t\t\t\tFUN CITY")
print("""------------------------------------------------------------------------""")
print("Main Menu")
print("What do you want to do?")
a=("Play a Game","Order Food","Use Splitwise","Use Love/Friendship Meter","Play a Quiz","Make a Graph")
for index, option in enumerate(a,start=1):
    print(f"{index}: {option}")
choice=int(input("Enter the number corresponding to your choice:"))
if choice==1:
    print("Welcome to Gamezone")
    print("Which Game do you want to play?")
    game=("Tic-Tac-Toe","Rock-Paper-Scissors","Number Guezz")
    for index, option in enumerate(game,start=1):
        print(f"{index}: {option}")
    choice=int(input("Enter the number corresponding to your choice:"))
    if choice==1:
        board=[[" " for _ in range(3)] for _ in range(3)]
        player1_symbol="X"
        player2_symbol="O"
        current_player=player1_symbol
        while True:
            try:
                print_board(board)
                row=int(input(f"Player {current_player}, enter row (1-3): "))
                col=int(input(f"Player {current_player}, enter column (1-3): "))
                row-=1
                col-=1
                if make_move(board,row,col,current_player):
                    if check_win(board,current_player):
                        print_board(board)
                        print(f"Player {current_player} wins!")
                        break
                    elif check_draw(board):
                        print_board(board)
                        print("It's a draw!")
                        break
                    current_player=player2_symbol if current_player == player1_symbol else player1_symbol
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid Input.Please enter 1, 2 or 3.")
            except IndexError:
                print("Invalid Input.Please enter 1, 2 or 3.")
    elif choice==2:
        choices=["rock", "paper", "scissors"]
        scores={"player": 0, "computer": 0, "tie": 0}
        print("Rock Paper Scissors Game!")
        print("Enter 'quit' to exit the game")
        while True:
            player_input=input("\nChoose rock, paper, or scissors: ").lower()
            if player_input=="quit":
                break
            if player_input not in choices:
                print("Invalid choice. Please try again.")
                continue
            computer_choice=random.choice(choices)
            print(f"\nYou chose: {player_input}")
            print(f"Computer chose: {computer_choice}")
            result=determine_winner(player_input, computer_choice)
            if result=="tie":
                print("It's a tie!")
            else:
                print(f"{result.capitalize()} wins this round!")
            scores[result]+=1
        
            print(f"\nCurrent scores:")
            print(f"Player: {scores['player']}  Computer: {scores['computer']}  Ties: {scores['tie']}")
    
        print("\nFinal Scores:")
        print(f"Player: {scores['player']}  Computer: {scores['computer']}  Ties: {scores['tie']}")
        print("Thanks for playing!")

    elif choice==3:
        choice=input("Would you like Normal or Hard Mode(N/H):").upper()
        if choice=='H':
            basic_game=NumberGuezz(1,100,10)
            basic_game.play()
        elif choice=='N':
            advanced_game=AdvancedNumberGuessGame(1, 100, 10)
            advanced_game.play()

elif choice==2:#Order
    food=("Order Burger","Order Pizza","Order Fries","Order Drink")
    for index, option in enumerate(food, start=1):
        print(f"{index}: {option}")
    choice=int(input("Enter the number corresponding to your choice:"))
    if choice==1:#Burger
        print("Welcome to Burgers Inn")
        no=int(input("Enter the number of burgers you would like to order:"))
        s=0
        while no>0:
            print("Which burger would you like to have?")
            burgers=("Aloo Tikki","Veggie","Paneer","Egg","Chicken","Double Cheese")
            for index, option in enumerate(burgers,start=1):
                print(f"{index}: {option}")
            choice=int(input("Enter the number corresponding to your choice:"))
            if choice==1:
                s+=50
                print("Aloo Tikki costs 50 rupees.")
            elif choice==2:
                s+=70
                print("Veggie costs 70 rupees.")
            elif choice==3:
                s+=90
                print("Veggie costs 90 rupees.")
            elif choice==4:
                s+=70
                print("Egg costs 70 rupees.")
            elif choice==5:
                s+=120
                print("Chicken costs 120 rupees.")
            elif choice==6:
                s+=70
                print("Double Cheese costs 70 rupees.")
            else:
                print("Invalid Choice")
                sys.exit(0)
            no-=1
        print(f"Your total is {s} rupees.\nYou will receive your order in less than 15 minutes.")
    elif choice==2:#Pizza
        print("Welcome to Pizza's Mania")
        s=0
        size=("4 Slices","6 Slices","8 Slices")
        for index, option in enumerate(size, start=1):
            print(f"{index}: {option}")
        choice=int(input("Enter the number corresponding to your choice:"))
        if choice==1:
            s+=100
        elif choice==2:
            s+=150
        elif choice==3:
            s+=180
        else:
            print("Invalid Choice.")
            sys.exit(0)
        p=input("Would you like to add Corn(Y/N):").upper()
        if p=="Y":
            s+=30
        elif p=="N":
            print("\t")
        else:
            print ("Invalid Choice.")
            sys.exit(0)
        p=input("Would you like to add Paneer(Y/N):").upper()
        if p=="Y":
            s+=50
        elif p=="N":
            print("\t")
        else:
            print ("Invalid Choice.")
            sys.exit(0)
        p=input("Would you like to add Chicken(Y/N):").upper()
        if p=="Y":
            s+=80
        elif p=="N":
            print("\t")
        else:
            print ("Invalid Choice.")
            sys.exit(0)
        p=input("Would you like to add Onion(Y/N):").upper()
        if p=="Y":
            s+=30
        elif p=="N":
            print("\t")
        else:
            print ("Invalid Choice.")
            sys.exit(0)
        p=input("Would you like to add Capsicum(Y/N):").upper()
        if p=="Y":
            s+=20
        elif p=="N":
            print("\t")
        else:
            print("Invalid Choice.")
            sys.exit(0)
        p=input("Would you like to add Olives(Y/N):").upper()
        if p=="Y":
            s+=40
        elif p=="N":
            print("\t")
        else:
            print ("Invalid Choice.")
            sys.exit(0)
        p=input("Would you like to add Cheese Burst(Y/N):").upper()
        if p=="Y":
            s+=80
        elif p=="N":
            print("\t")
        else:
            print ("Invalid Choice.")
            sys.exit(0)
        print(f"Your total is {s} rupees.\nYou will receive your order in less than 30 minutes.")
    elif choice==3:#Fries
        print("Welcome to Fried Fries")
        fries=("Salted","Cheesy","Peri-Peri","Zig-Zag")
        s=0
        for index, option in enumerate(fries, start=1):
            print(f"{index}: {option}")
        choice=int(input("Enter the number corresponding to your choice:"))
        if choice==1:
            s+=50
        elif choice==2:
            s+=100
        elif choice==3:
            s+=80
        elif choice==4:
            s+=70
        else:
            print("Invalid Choice.")
            sys.exit(0)
        print(f"Your total is {s} rupees.\nYou will receive your order in less than 15 minutes.")
    elif choice==4:#Drinks
        print("Welcome to Drinks")
        drinks=("Coke","Lassi","Pepsi","Fanta","Orange Juice","Mango Juice","Chocolate Shake","Oreo Shake","Kit Kat Shake","Strawberry Shake","Mango Shake","Baadaam Milk")
        s=0
        no=int(input("Enter number of drinks you would like to order:"))
        while no>0:
            for index, option in enumerate(drinks, start=1):
                print(f"{index}: {option}")
            choice=int(input("Enter the number corresponding to your choice:"))
            if choice==1:
                s+=50
            elif choice==2:
                s+=80
            elif choice==3:
                s+=50
            elif choice==4:
                s+=50
            elif choice==5:
                s+=70
            elif choice==6:
                s+=70
            elif choice==7:
                s+=100
            elif choice==8:
                s+=100
            elif choice==9:
                s+=100
            elif choice==10:
                s+=90
            elif choice==11:
                s+=90
            elif choice==12:
                s+=90
            else:
                print("Invalid Choice.")
                sys.exit(0)
            no-=1
        print(f"Your total is {s} rupees.\nYou will receive your order in less than 10 minutes.")
    else:
        print("Invalid Choice.")
        sys.exit(0)
        
elif choice==3:#Splitwise
    print("Handle Group Spending With Ease\n\t\tSplitwise")
    no=int(input("How many members are there in the group?"))
    friends={}
    total=0
    currency=input("Enter Currency:")
    members(no)
    expense(total,no)
elif choice==4:#Meter
    choice=input("Would you like use love or friendship meter?(L/F)").upper()
    m=0
    if choice=="L":
        n1=input("Enter Name 1:").upper()
        n2=input("Enter Name 2:").upper()
        for i in n1:
            if i=="L" or  i=="O" or i=="V" or i=="E":
                m+=1
        for i in n2:
            if i=="L" or  i=="O" or i=="V" or i=="E":
                m+=1
        if m>10:
            m=m/10+m%10
        if m>=0 and m<=3:
            print (f"Your score is {m}.")
            print("You will face problems.But dont give up!\nKeep Going!")
        elif m>3 and m<=6:
            print (f"Your score is {m}.")
            print("Congrats! You are made for each other!")
        elif m>6 and m<=9:
            print (f"Your score is {m}.")
            print("You will face problems.But dont give up!\nKeep Going!")
    elif choice=="F":
        n1=input("Enter Name 1:").upper()
        n2=input("Enter Name 2:").upper()
        for i in n1:
            if i=="F" or  i=="R" or i=="I" or i=="E" or i=="N" or i=="D":
                m+=1
        for i in n2:
            if i=="F" or  i=="R" or i=="I" or i=="E" or i=="N" or i=="D":
                m+=1
        if m>10:
            m=m/10+m%10
        if m>=1 and m<=3:
            print (f"Your score is {m}.")
            print("You will have some different opinions but you can make it work.")
        elif m>3 and m<=6:
            print (f"Your score is {m}.")
            print("Congrats! You are like siblings!")
        elif m>6 and m<=9:
            print (f"Your score is {m}.")
            print("You will have some different opinions but you can make it work.")
    else:
        print("Invalid choice")
        sys.exit(0)
elif choice==5:#Quiz
    choose()
elif choice==6:
    data = {
        "Game": ["Tic-Tac-Toe","Rock-Paper-Scissors","Number Guess"],
        "Score": [random.randint(1, 100),random.randint(1, 100),random.randint(1, 100)]
    }
    df=pd.DataFrame(data)
    plt.figure(figsize=(8,6))
    plt.bar(df["Game"],df["Score"],color="skyblue")
    plt.xlabel("Game")
    plt.ylabel("Score")
    plt.title("Game Scores")
    plt.show()
else:
    print("Invalid Choice.")
