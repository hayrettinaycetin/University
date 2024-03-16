def reverse_text(text):
    digit_map = {'0': '9', '1': '8', '2': '7', '3': '6',
                  '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', '9': '0'}
    reversed_text = ''
    for char in text:
        if char.isdigit() and char in digit_map:
            reversed_text += digit_map[char]  
        else:
            reversed_text += char
    return reversed_text[::-1]

user_input = input("Please enter text: ")
reversed_input = reverse_text(user_input)

print("Reversed text: " + reversed_input)
