with open('filtered.txt', 'r', encoding='utf-8') as past_file:
    past_words = past_file.read().split()

with open('checkf.txt', 'r', encoding='utf-8') as input_file:
    input_words = input_file.read().split()

past_tense_words = [word for word in input_words if word in past_words]

print(f"The following words are past tense: {past_tense_words}")
