from random import randint

rock = 0
paper = 1
scisors = 2


def game_rock_paper_scisors(user_input: int):
    pc_choose = randint(0, 2)

    if user_input == pc_choose:
        #It is a DRAW
        return None
    elif user_input == 1 and pc_choose == 0:
        # Paper beats Rock, user wins
        return True
    elif user_input == 2 and pc_choose == 1:
        # Scissors beats Paper, user wins
        return True
    elif user_input == 0 and pc_choose == 2:
        #Rock  beats Scissors, user wins
        return True
    else:
        # User loses
        return False   


def game_result(game_output):
    if game_output is None:
        return "It is a DRAW"
    elif game_output:
        return "User wins"
    else:
        return "User loses"


def game_ask_user():
    user_input_str = "" 

    while not isinstance(user_input_str, int):
        user_input_str = input("Choose to play 0 - Rock, 1 - Paper, 2 - Scissors: ")
    
        try:
            user_input_str = int(user_input_str)
            if not 0 <= user_input_str <= 2:
                user_input_str = ""
                print("Try agian but in range 0 to 2 inclusive")

        except:
            print("Try agian")

    game_output = game_rock_paper_scisors(int(user_input_str))
    print(game_result(game_output))

game_ask_user()

