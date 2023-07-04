import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize,sent_tokenize

text="Hello, how are you?"
tokens=word_tokenize(text)
print(tokens)

text = "I love pizza. It's my favorite food."
sentences = sent_tokenize(text)
print(sentences)