# import these modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize #for tokenization 
from functools import reduce #for reducing the sentence

ps = PorterStemmer()

# choose some words to be stemmed
words = ["program", "programs", "programmer", "programming", "programmers"]
terms = ['runs', 'running' , 'runner', 'runnn']
names = ['likes', 'liked', 'likely', 'liking']

for w in words:
	print(w, " : ", ps.stem(w))

for t in terms:
    print(t, ':', ps.stem(t))
    
for n in names:
    print(n, ':', ps.stem(n))    
    
#STEMMING OF SENTENCE
sentence = "Programmers program with programming languages"
words = word_tokenize(sentence)
 
# using reduce to apply stemmer to each word and join them back into a string
stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), words, "")
 
print(stemmed_sentence)    

#Stemming using SnowballStemmer algorithm 
from nltk.stem import SnowballStemmer

# Choose a language for stemming, for example, English
stemmer = SnowballStemmer(language='english')

# Example words to stem
words_to_stem = ['running', 'jumped', 'happily', 'quickly', 'foxes']

# Apply Snowball Stemmer
stemmed_words = [stemmer.stem(word) for word in words_to_stem]

# Print the results
print("Original words:", words_to_stem)
print("Stemmed words:", stemmed_words)

#STEMMING USING LANCESTAR STEMMER ALGORITHM 
from nltk.stem import LancasterStemmer

# Create a Lancaster Stemmer instance
stemmer = LancasterStemmer()

# Example words to stem
words_to_stem = ['running', 'jumped', 'happily', 'quickly', 'foxes']

# Apply Lancaster Stemmer
stemmed_words = [stemmer.stem(word) for word in words_to_stem]

# Print the results
print("Original words:", words_to_stem)
print("Stemmed words 1:", stemmed_words)

#STEMMING USING REGEXSTEMMER
from nltk.stem import RegexpStemmer

# Create a Regexp Stemmer with a custom rule
custom_rule = r'ing$'
regexp_stemmer = RegexpStemmer(custom_rule)

# Apply the stemmer to a word
word = 'running'
stemmed_word = regexp_stemmer.stem(word)

print(f'Original Word: {word}')
print(f'Stemmed Word 2: {stemmed_word}')
