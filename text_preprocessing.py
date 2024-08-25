import emoji
import re
import string
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import contractions
#from spellchecker import SpellChecker

# Ensure nltk packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample corpus with an emoji
corpus = [
    "I can't wait for the new season of my favorite show! The new season has to be everyone's favorite",
    "The COVID-19 pandemic has affected millions of people worldwide. This was the worst pandemic.",
    "U.S. stocks fell on Friday after news of rising inflation. The news shocked everyone in U.S.",
    "<html><body>Welcome to the website, we are elated to have you!</body></html>",
    "Python is a great programming language!!! ??", 
    "Text preprocessing is fun!!!",
    emoji.emojize("Python is amazing :red_heart: ") , # Using emoji 
    emoji.emojize("Text preprocessing is fun :thumbs_up: ")  # Using emoji
]

def clean_text(text):
    text = text.lower()  # Lowercase
    text = contractions.fix(text)  # Expand contractions (e.g., can't -> cannot)
    text = BeautifulSoup(text, "html.parser").get_text()  # Remove HTML tags
    text = re.sub(r'\d+', '', text)  # Remove numbers
    # Removing punctuation while retaining emojis
    text = text.translate(str.maketrans('', '', string.punctuation.replace(':', ''))) 
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text

# Clean the corpus
cleaned_corpus = [clean_text(doc) for doc in corpus]
print("Cleaned Corpus:")
print(cleaned_corpus)

# Tokenization
tokenized_corpus = [word_tokenize(doc) for doc in cleaned_corpus]
print("Tokenized Corpus:")
print(tokenized_corpus)

# Stop Words Removal
stop_words = set(stopwords.words('english'))
filtered_corpus = [[word for word in doc if word not in stop_words] for doc in tokenized_corpus]
print("Filtered Corpus:")
print(filtered_corpus)

# Stemming and Lemmatization
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_corpus = [[stemmer.stem(word) for word in doc] for doc in filtered_corpus]
lemmatized_corpus = [[lemmatizer.lemmatize(word) for word in doc] for doc in filtered_corpus]
print("Stemmed Corpus:")
print(stemmed_corpus)
print("Lemmatized Corpus:")
print(lemmatized_corpus)

# Contraction Expansion
expanded_corpus = [contractions.fix(doc) for doc in cleaned_corpus]
print("Expanded Corpus:")
print(expanded_corpus)

# Emoji handling
emoji_corpus = [emoji.demojize(doc) for doc in cleaned_corpus]
print("Emoji Corpus:")
print(emoji_corpus)


