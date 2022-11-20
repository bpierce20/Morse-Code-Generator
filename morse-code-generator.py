
# Dictionary for morse code

morse_code_dictionary = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

# Ask for user input
ans = input('Morse Code Converter\nType text to convert to Morse Code!\n')
# Creates a list called output_list
output_list = []

# For each letter in the users input, first make it lower case, then append each letter to the output_list


def text_to_morse():
    for letter in ans:
        letter = letter.lower()
        output_list.append(morse_code_dictionary[letter])


# Call text_to_morse() method
text_to_morse()

# The result for each letter is joined by a space
result = ' '.join(output_list)
print(f'The Morse Code of {ans} is {result}')

print("Wow! You're amazin!")
print("Wow3")
