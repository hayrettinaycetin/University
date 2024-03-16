class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def input_word_and_multipliers(self):
        print(f"\n{self.name}'s Turn:")
        self.word = input("Please enter the word that you want to learn the score: ")
        print("2X OR 3X WORD.")
        print("PLEASE ENTER 0 FOR NOT HAVING")
        self.double_word = int(input("Double Word Numbers: "))
        self.triple_word = int(input("Triple Word Numbers: "))

    def calculate_score(self):
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

        for char in self.word:
            char_lower = char.lower()
            if char_lower in char_scores:
                score += char_scores[char_lower]

        return score

    def calculate_final_score(self):
        without_score_words = self.calculate_score()

        if self.double_word != 0:
            without_score_words = self.double_word * without_score_words * 2

        if self.triple_word != 0:
            without_score_words = self.triple_word * without_score_words * 3

        self.score = without_score_words
        return without_score_words

    def display_final_score(self):
        print(f"\n{self.name}'s Final Score:", self.score)


def main():
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    players = [player1, player2]
    current_player = 0

    while True:
        current_player_instance = players[current_player]

        print("\nMenu:")
        print("1. Enter word and multipliers")
        print("2. Calculate and display final score")
        print("3. Exit")

        choice = input(f"{current_player_instance.name}, enter your choice (1-3): ")

        if choice == "1":
            current_player_instance.input_word_and_multipliers()
        elif choice == "2":
            current_player_instance.calculate_final_score()
            current_player_instance.display_final_score()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

        current_player = (current_player + 1) % len(players)


if __name__ == "__main__":
    main()
