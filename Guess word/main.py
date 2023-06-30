import random

easy_level_guess=10
hard_level_guess=5
turns = 0

def set_difficulty():
    level=input("choose the level of difficulty that is 'easy' or 'hard'")
    if level=="easy":
        print(f"your total guesses is {easy_level_guess}")
        return easy_level_guess
    else :
        print(f"your total guesses is {hard_level_guess} ")
        return hard_level_guess

def check_answer(user_guess,comp_guess,turns):
    if user_guess>comp_guess:
        print("too high")
        return turns-1
    elif user_guess<comp_guess:
        print("too low")
        return turns - 1
    else:
        print("congratulation! you won.")

def game():
    print("welcome to the guess game you have to guess a number until you guess is over")

    comp_guess=random.randint(1,101)
    print(comp_guess)
    turns=set_difficulty() # give back the num of turns     # calling first function
    print(f'you have {turns} turns')

    user_guess=0
    while user_guess!= comp_guess:
        user_guess=int(input("enter your guess "))
        turns=check_answer(user_guess,comp_guess,turns)# give us number of turns - 1 and (user,comp guess comparison) #calls second function

        print(f'your remaining turns is {turns}')
        if turns==0:
            print('game over ! try again')
        return

game()
