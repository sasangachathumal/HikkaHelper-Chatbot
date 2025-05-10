# download_nltk_resources.py

import nltk
import ssl

def download_resources():
    """Downloads the required NLTK resources if they are not already present."""

    # Create an unverified SSL context
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    resources_to_download = [
        ('tokenizers/punkt', 'punkt'),
        ('corpora/wordnet', 'wordnet'),
        ('corpora/stopwords', 'stopwords'),
    ]

    for path, resource_name in resources_to_download:
        try:
            nltk.data.find(path)
        except LookupError:
            print(f"Downloading NLTK resource: {resource_name}")
            nltk.download(resource_name)
        else:
            print(f"NLTK resource '{resource_name}' already downloaded.")

if __name__ == '__main__':
    download_resources()
    print("Finished checking and downloading NLTK resources.")