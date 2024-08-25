# import the required libraries
import nltk
nltk.download('punkt') # punkt tokenizer for sentence tokenization
nltk.download('stopwords') # list of stop words, such as 'a', 'an', 'the', 'in', etc, which would be dropped
from collections import Counter # Imports the Counter class from the collections module, used for counting the frequency of words in a text.
from nltk.corpus import stopwords # Imports the stop words list from the NLTK corpus
# corpus is a large collection of text or speech data used for statistical analysis

from nltk.tokenize import sent_tokenize, word_tokenize # Imports the sentence tokenizer and word tokenizer from the NLTK tokenizer module. 
# Sentence tokenizer is for splitting text into sentences
# word tokenizer is for splitting sentences into words

# this function would take 2 inputs, one being the text, and the other being the summary which would contain the number of lines
def generate_summary(text, n):
    # Tokenize the text into individual sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into individual words and remove stopwords
    stop_words = set(stopwords.words('english'))
    # the following line would tokenize each sentence from sentences into individual words using the word_tokenize function of nltk.tokenize module
    # Then removes any stop words and non-alphanumeric characters from the resulting list of words and converts them all to lowercase
    words = [word.lower() for word in word_tokenize(text) if word.lower() not in stop_words and word.isalnum()]
    
    # Compute the frequency of each word
    word_freq = Counter(words)
    
# Compute the score for each sentence based on the frequency of its words
# After this block of code is executed, sentence_scores will contain the scores of each sentence in the given text, 
# where each score is a sum of the frequency counts of its constituent words

    # empty dictionary to store the scores for each sentence
    sentence_scores = {}

    for sentence in sentences:
        sentence_words = [word.lower() for word in word_tokenize(sentence) if word.lower() not in stop_words and word.isalnum()]
        sentence_score = sum([word_freq[word] for word in sentence_words])
        if len(sentence_words) < 20:
            sentence_scores[sentence] = sentence_score
    
# checks if the length of the sentence_words list is less than 20 (parameter can be adjusted based on the desired length of summary sentences)
# If condition -> true, score of the current sentence is added to the sentence_scores dictionary with the sentence itself as the key
# This is to filter out very short sentences that may not provide meaningful information for summary generation

    # Select the top n sentences with the highest scores
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
    summary = ' '.join(summary_sentences)
    
    return summary


text = '''
Weather is the day-to-day or hour-to-hour change in the atmosphere. 
Weather includes wind, lightning, storms, hurricanes, tornadoes (also known as twisters), rain, hail, snow, and lots more. 
Energy from the Sun affects the weather too. 
Climate tells us what kinds of weather usually happen in an area at different times of the year. 
Changes in weather can affect our mood and life. We wear different clothes and do different things in different weather conditions. 
We choose different foods in different seasons.
Weather stations around the world measure different parts of weather. 
Ways to measure weather are wind speed, wind direction, temperature and humidity. 
People try to use these measurements to make weather forecasts for the future. 
These people are scientists that are called meteorologists. 
They use computers to build large mathematical models to follow weather trends.'''

summary = generate_summary(text, 5)
summary_sentences = summary.split('. ')
formatted_summary = '.\n'.join(summary_sentences)

print(formatted_summary)