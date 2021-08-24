
HANGMAN_ASCII_ART = '''
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |  
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
    '''

MAX_TRIES = 6

PIC1 = '''
    x-------x
        '''
PIC2 = '''
    x-------x
    |
    |
    |
    |
    |
                  '''

PIC3 = '''
    x-------x
    |       |
    |       0
    |
    |
    |
                    '''

PIC4 = '''
    x-------x
    |       |
    |       0
    |       |
    |
    |
                    '''
PIC5 = '''
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
                    ''' 
PIC6 = '''
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
                   '''
PIC7 = '''        
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |

                    '''
    
HANGMAN_PHOTOS = {0:PIC1,
                  1:PIC2,
                  2:PIC3,
                  3:PIC4,
                  4:PIC5,
                  5:PIC6,
                  6:PIC7}
                  
            


def choose_word(file_path, index):
    with open(file_path, "r") as words_file:
        words_list = words_file.read().split(" ")
        words_only_once_list = []
        for word in words_list:
            if not(word in words_only_once_list):
                words_only_once_list.append(word)
        words_num = len(words_only_once_list)
        word = words_list[(index - 1) % len(words_list)]
        return (words_num, word)
        
        
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def check_valid_input(letter_guessed, old_letter_guessed):
    '''check if guessed letter meets all the requirements.
    :param letter_guessed: The letter the player has just guessed
    :param old_letter_guessed: A list of letters the player has guessed earlier  
    :type letter_guessed: str
    :type old_letter_guessed
    :return: return True if letter_guessed is a one english letter and hasen't been guessed before. else, False will be returned.
    :rtype: bool
    '''
    if (len(letter_guessed) == 1) and (letter_guessed.isalpha()) and (letter_guessed not in old_letter_guessed):
        return True
    else:
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    secret_word_by_lines = ["_"] * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            secret_word_by_lines[i] = secret_word[i]
    secret_word_by_lines = " ".join(secret_word_by_lines) 
    return secret_word_by_lines
            
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if not(letter in old_letters_guessed):
            return False
    return True

def main():
    print(f"{HANGMAN_ASCII_ART} \n {MAX_TRIES}")
    txt_path = input('Enter a file path: ')
    word_number = int(input("Enter a word number: "))
    secret_word = choose_word(txt_path, word_number)[1]
    print_hangman(0)
    wrong_num = 0
    old_letters_guessed = []
    print(show_hidden_word(secret_word, old_letters_guessed))
    while wrong_num < 6:
        letter_guessed = input("Enter a letter: ")
        while not(check_valid_input(letter_guessed, old_letters_guessed)):
            print("X")
            print(" -> ".join(sorted(old_letters_guessed)))
            letter_guessed = input("Enter a letter: ")
        old_letters_guessed.append(letter_guessed)
        if letter_guessed in secret_word:
            print(show_hidden_word(secret_word, old_letters_guessed))
        else:
            print("):")
            wrong_num += 1
            print_hangman(wrong_num)
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            break
    if not(check_win(secret_word, old_letters_guessed)):
        print("LOOSE")
        
if __name__ == "__main__":
    main()



