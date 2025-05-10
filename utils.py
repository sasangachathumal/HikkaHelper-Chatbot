import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class TextPreprocessor:
    def __init__(self, language='english'):
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = set(stopwords.words(language)) # You can keep this if you decide to use it later

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

if __name__ == '__main__':
    processor = TextPreprocessor()
    text1 = "Running quickly through the park, the dogs were happy."
    processed_text1 = processor.preprocess(text1)
    print(f"Original: {text1}")
    print(f"Processed: {processed_text1}")

    text2 = "What are some interesting activities to do in Hikkaduwa?"
    processed_text2 = processor.preprocess(text2)
    print(f"Original: {text2}")
    print(f"Processed: {processed_text2}")