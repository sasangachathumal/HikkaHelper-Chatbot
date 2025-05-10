import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class TextPreprocessor:
    def __init__(self, language='english'):
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = set(stopwords.words(language))

    def preprocess(self, text):
        print(f"PREPROCESS: Input text - '{text}'")
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        print(f"PREPROCESS: Tokenized - '{tokens}'")
        processed_tokens = []
        for word in tokens:
            print(f"PREPROCESS: Examining word - '{word}'")
            if word.isalpha(): # Only check if it's alphabetic before lemmatizing
                print(f"PREPROCESS: '{word}' is alpha.")
                lemmatized_word = self.lemmatizer.lemmatize(word)
                processed_tokens.append(lemmatized_word)
                print(f"PREPROCESS: Lemmatized '{word}' to '{lemmatized_word}'")
            else:
                print(f"PREPROCESS: '{word}' is not alpha.")
        print(f"PREPROCESS: Lemmatized tokens - '{' '.join(processed_tokens)}'")
        return " ".join(processed_tokens)