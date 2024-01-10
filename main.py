from letter_state import LetterState
from wordle import Wordle
import random
from colorama import Fore

def main():
    word_set = load_word_set("data/wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)
    
    while wordle.can_attempt:
        word = str(input("Type your guess: ")).upper()
        if len(word) != wordle.WORD_LENGHT:
            print(f"The word must be {wordle.WORD_LENGHT} characters long.")
            continue
        if word not in list(word_set):
            print(f"{word} is not allowed")
            continue
        
        wordle.attempt(word)
        display_attempts(wordle)
        
    if wordle.is_solved:
        print("Solved, NICE!")
    else:
        print("Failed, BADDDDD!")
        print("The right word was " + secret)

def display_attempts(wordle: Wordle):
    for word in wordle.attempts:
       result = wordle.guess(word)
       colored_result = convert_result_with_color(result)
       print(colored_result)
    for _ in range(wordle.remeaning_attempts):
        print("_" * wordle.WORD_LENGHT)

def convert_result_with_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.char + Fore.RESET
        result_with_color.append(colored_letter)
    return "".join(result_with_color)

def load_word_set(path: str):
    word_set = set()
    with open(path, 'r') as f:
        for line in f:
            word = line.strip().upper()
            word_set.add(word)
    return word_set

if __name__ == "__main__":
    main()