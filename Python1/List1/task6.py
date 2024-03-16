print("$$ Scrabble Word Score Caclulator $$")
word = input("Please enter the word that you want to learn the score ")
print("2X OR 3X WORD.")
print("PLEASE ENTER 0 FOR NOT HAVING")
double_word =int(input("Double Word Numbers: "))
triple_word = int(input("Triple Word Numbers: "))

def calculate_score(word):
    char_scores = {
        "a": 1, "e": 1, "i": 1, "l": 1, "n": 1, "o": 1, "r": 1, "s": 1, "t": 1, "u": 1,
        "d": 2, "g": 2,
        "b": 3, "c": 3, "m": 3, "p": 3,
        "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
        "k": 5,
        "j": 8, "x": 8,
        "q": 10, "z": 10,
    }

    score = 0

    for char in word:
        char_lower = char.lower()  
        if char_lower in char_scores:
            score += char_scores[char_lower]
    
    return score

without_score_words = calculate_score(word)

while double_word != 0:
    without_score_words = double_word * without_score_words * 2 
    double_word = 0
    break


while triple_word != 0:
    without_score_words = triple_word * without_score_words *3
    triple_word = 0
    break

print(without_score_words)