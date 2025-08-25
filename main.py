from random import randint

rock = 0
paper = 1
scisors = 2


def game_rock_paper_scisors(user_input: int):
    pc_choose = randint(0, 2)

    if user_input == pc_choose:
        # It is a DRAW
        return None
    elif user_input == 1 and pc_choose == 0:
        # Paper beats Rock, user wins
        return True
    elif user_input == 2 and pc_choose == 1:
        # Scissors beats Paper, user wins
        return True
    elif user_input == 0 and pc_choose == 2:
        # Rock  beats Scissors, user wins
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


def print_main_task(word, rez_list, search_list=[]):
    if len(search_list):
        for i in range(len(word)):
            if i in search_list:
                rez_list[i] = word[i]

    print(f"\nGuess the word \t {" ".join(rez_list)}")


def game_wonder_field_rezult_out(word, search_list, rez_list):
    print_main_task(word, search_list, rez_list)
    if len(search_list):
        print(f"\nGongratulations: you guessed the letter ")
    else:
        print(f"There is no such character in this word")


def search_char_in_word(word: str, char: str, list, start: int = 0):
    position = word.find(char.upper(), start)
    if position != -1:
        list.append(position)
        search_char_in_word(word, char, list, position + 1)


def ask_user_character(word, rez_list):
    index_search = []
    user_input = ""
    while len(user_input) == 0:
        user_input = input("Enter your charcter: ")

        if len(user_input) == 1:
            if ord(user_input.upper()) >= ord("A") and ord(user_input.upper()) <= ord(
                "Z"
            ):
                if user_input.upper() in rez_list:
                    print("You have already entered this character. Try agian.")
                    user_input = ""
                else:
                    break
            else:
                print("Try agian but only letters from 'A' to 'Z'")
                user_input = ""
        else:
            print("Try agian but only one letter from 'A' to 'Z'")
            user_input = ""

    search_char_in_word(word, user_input, index_search)
    game_wonder_field_rezult_out(word, rez_list, index_search)


def ask_user_word(word, rez_list):
    index_search = []
    user_input = ""
    while len(user_input) == 0:
        user_input = input("Enter your  word: ")

        if len(user_input) == len(word):
            for i in user_input:
                if not (ord(i.upper()) >= ord("A") and ord(i.upper()) <= ord("Z")):
                    #                    pass
                    #                else:
                    print("Try agian but only letters from 'A' to 'Z'")
                    user_input = ""
                    break
            if len(user_input):
                break
        else:
            print(
                f"Try agian but enter whole word {len(word)} letters only one letter from 'A' to 'Z'"
            )
            user_input = ""

    if user_input.upper() == word:
        index_search.extend(list(range(0, len(word))))
        game_wonder_field_rezult_out(word, rez_list, index_search)


if __name__ == "__main__":
    word = "Developer"
    word = word.upper()
    rez_list = ["*"] * len(word)
    print_main_task(word, rez_list)
    while "*" in rez_list:
        if rez_list.count("*") < len(rez_list):
            user_input = input("\nAre you ready to say the word (Y/N): ")
            if user_input.upper() == "Y":
                ask_user_word(word, rez_list)
            else:
                ask_user_character(word, rez_list)
        else:
            ask_user_character(word, rez_list)

    print(f"\nGongratulations: you guessed the Word ")
