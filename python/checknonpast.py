import nltk

english_verbs = set(w.lower() for w in nltk.corpus.words.words() if nltk.pos_tag([w])[0][1].startswith('V'))

with open('checkf.txt', 'r', encoding='utf-8') as input_file:
    input_words = input_file.read().split()

with open('filtered.txt', 'r', encoding='utf-8') as past_file:
    past_words = past_file.read().split()

non_past_tense_words = [word for word in input_words if word not in past_words and word.lower() in english_verbs]

print("The following English verbs are not in the past tense:")
print(non_past_tense_words)