from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Malayalam"
html=urlopen(url).read()
soup=BeautifulSoup(html)
for script in soup(["script","style"]):
    script.extract()
text=soup.get_text()
lines=(line.strip() for line in text.splitlines())
chunks=(phrase.strip() for line in lines for phrase in line.split(" "))
text='\n'.join(chunk for chunk in chunks if chunk)
print(text)
#SENTENCE TOKENIZATION
from nltk.tokenize import sent_tokenize
sent_tokenize_list = sent_tokenize(text)
print(sent_tokenize_list)
for i in sent_tokenize_list:
    print(i)
#WORD TOKENIZER
from nltk.tokenize import word_tokenize
word_tokenize(text)
#PUNCTUATION TOKENIZER
from nltk.tokenize import WordPunctTokenizer
word_punct_tokenizer = WordPunctTokenizer()
word_punct_tokenizer.tokenize(text)
for i in word_punct_tokenizer.tokenize(text):
    print(i)