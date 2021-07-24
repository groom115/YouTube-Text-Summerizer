
#getting the frequency of words
def freq(text):
  nlp = spacy.load('en_core_web_sm')
  doc = nlp(text)
  tokens = [token.text for token in doc]
          
  word_frequencies = {}
            
  for word in doc:
    if word.text.lower() not in punctuation:
       if word.text not in word_frequencies.keys():
         word_frequencies[word.text] = 1
       else:
         word_frequencies[word.text] += 1
                            
  max_frequency = max(word_frequencies.values())
  #print(max_frequency
  
  #normalising frequency
  for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

  return word_frequencies
  
  
 #finding the scores of each sentence
  def sentence(text):
    word_frequencies = {}
    word_frequencies=freq(text)

    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
        
    for sent in sentence_tokens:
      for word in sent:
        if word.text.lower() in word_frequencies.keys():
          if sent not in sentence_scores.keys():
            sentence_scores[sent] = word_frequencies[word.text.lower()]
          else:
            sentence_scores[sent] += word_frequencies[word.text.lower()]

  #print(sentence_scores)
   return sentence_scores ,sentence_tokens
  
  
  
  def Extractive(url,freq):
  
    text=get_transcript(url)
    clean_text=clean_body(text)
  
    sentence_scores = {}
    sentence_scores ,sentence_tokens=sentence(text)

    from heapq import nlargest
    select_length = int(len(sentence_tokens)*freq)
  
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
        
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
            
# return summary
    return summary
  
 
#getting the url link and oassing throuh summerizer
#url="https://www.youtube.com/watch?v=erx9czQsY2Q"
print(Extractive(url,0.1))
