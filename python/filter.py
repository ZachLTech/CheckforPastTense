with open('allwords.txt', 'r') as input_file:
    all_words = input_file.read().split()

past_tense_words = [word for word in all_words if word.endswith('ed')]

with open('filteredpasttense.txt', 'w') as output_file:
    output_file.write('\n'.join(past_tense_words))