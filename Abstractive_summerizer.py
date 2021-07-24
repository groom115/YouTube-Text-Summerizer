from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig
tokenizer=BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model=BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')



def abs():
  text=get_transcript(url)
  original_text=clean_body(text)
  inputs = tokenizer.batch_encode_plus([original_text],return_tensors='pt')
  summary_ids = model.generate(inputs['input_ids'], early_stopping=True)
  bart_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
  return bart_summary

