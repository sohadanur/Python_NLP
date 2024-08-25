# Python3 code for preprocessing text 
''' We will first preprocess the data, in order to:
Convert text to lower case.
Remove all non-word characters.
Remove all punctuations

import nltk 
import re 
import numpy as np 

# execute the text here as : 
text = "Beans. I was trying to explain to somebody as we were flying in that’s corn. That’s beans. And they were very impressed at my agricultural knowledge.Please give it up for Amaury once again for that outstanding introduction. I have a bunch of good friends here today, including somebody who I served , with who is one of the finest senators in the country, and we’re lucky to have him"
dataset = nltk.sent_tokenize(text) 
for i in range(len(dataset)): 
	dataset[i] = dataset[i].lower() 
	dataset[i] = re.sub(r'\W', ' ', dataset[i]) 
	dataset[i] = re.sub(r'\s+', ' ', dataset[i]) 
 
print("This is the original text; ", text)
print ("This is the dataset: ", dataset)'''

import nltk
import re

# Ensure NLTK resources are downloaded
nltk.download('punkt')

# Example text
text = ("Beans. I was trying to explain to somebody as we were flying in that’s corn. "
        "That’s beans. And they were very impressed at my agricultural knowledge. "
        "Please give it up for Amaury once again for that outstanding introduction. "
        "I have a bunch of good friends here today, including somebody who I served with, "
        "who is one of the finest senators in the country, and we’re lucky to have him.")

# Tokenize the text into sentences
dataset = nltk.sent_tokenize(text)

# Process each sentence
#The first line removes single alphabetic characters surrounded by spaces.
#The second line replaces non-word characters with spaces.
#The third line ensures that there are no multiple spaces in a row and 
# trims the string of any extra spaces at the beginning or end.
for i in range(len(dataset)):
    # Convert to lowercase
    dataset[i] = dataset[i].lower()
    # Remove all non-word characters (everything except numbers and letters)
    dataset[i] = re.sub(r'\W', ' ', dataset[i])
    # Remove all single characters
    #This line removes any single alphabetic characters (like "a", "I", etc.) that are surrounded by spaces.
    '''\s+ matches one or more whitespace characters (spaces, tabs, etc.).
    [a-zA-Z] matches any single alphabetic character.
    \s+ following the alphabetic character ensures that it is surrounded by spaces.
    sub() replaces the entire matched pattern with a single space.'''
    dataset[i] = re.sub(r'\s+[a-zA-Z]\s+', ' ', dataset[i])
    # Replace multiple spaces with a single space
    #.strip() removes any leading or trailing spaces from the resulting string.
    dataset[i] = re.sub(r'\s+', ' ', dataset[i]).strip()
    
    words = nltk.word_tokenize(dataset[i])
    print(words)

# Display the result
for sentence in dataset:
    print(sentence)
