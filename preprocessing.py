import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


# preprocessing the data
def clean_body(text):
    newText = text.lower()
    newText = re.sub('[^\w\s\d\.]',' ',newText)
    newText = ' '.join(newText.split())
    tokens = [w for w in newText.split() if not w in STOP_WORDS]
    long_words=[]
    for i in tokens:
        if len(i)>=2:
            long_words.append(i)   
    return (" ".join(long_words)).strip()
    return text
#print(clean_body(text))
