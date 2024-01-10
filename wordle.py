from letter_state import LetterState

class Wordle:
    
    MAX_ATTEMPTS = 6
    WORD_LENGHT = 5
    
    def __init__(self, secret: str):
        self.secret = secret.upper()
        self.attempts = []
    
    def attempt(self, word: str):
        self.attempts.append(word)
    
    def guess(self, word: str):
        word = word.upper()
        result = []
        for i in range(self.WORD_LENGHT):
            letter = LetterState(word[i])
            letter.is_in_position = word[i] == self.secret[i]
            letter.is_in_word = word[i] in self.secret
            result.append(letter)
        
        return result
    
    @property
    def is_solved(self):
        return self.secret in self.attempts
    
    @property
    def remeaning_attempts(self):
        return self.MAX_ATTEMPTS - len(self.attempts)
    
    @property
    def can_attempt(self):
        return self.remeaning_attempts > 0 and not self.is_solved