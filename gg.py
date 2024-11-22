import pandas as pd
vowels = set('аеєиіїоуюя')

def сheck(word):
    count = sum(1 for char in word.lower() if char in vowels)
    return count >= 3

with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

words = pd.Series([word for line in lines for word in line.split()])

filtered_words = words[words.apply(сheck)]

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(filtered_words))
    
print("Слова, що містять 3 або більше голосних, записані у файл 'output.txt'.")