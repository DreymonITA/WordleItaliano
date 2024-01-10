class LetterState:
    def __init__(self, char: str):
        self.char = char
        self.is_in_word = False
        self.is_in_position = False
    
    def __repr__(self):
        return f"[{self.char} is_in_word: {self.is_in_word} is_in_position: {self.is_in_position}]"