import string

with open('checkp.txt', 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# Remove all punctuation and quotation marks from the text
translator = str.maketrans('', '', string.punctuation + "\"'")
input_text = input_text.translate(translator)

# Replace all spaces with newline characters
input_text = input_text.replace(' ', '\n')

with open('checkf.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(input_text)

print("The cleaned text has been saved to checkf.txt.")