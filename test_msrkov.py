import markovify
#import nagisa
from janome.tokenizer import Tokenizer

with open("./test.txt", encoding="utf-8") as f:
	text = f.read()

#text_model = markovify.Text(text)
text_model = markovify.NewlineText(text)

for i in range(5):
	print(text_model.make_sentence())

"""
#Mecabで日本語の品詞分解
with open("./mecab.txt", encoding="utf-8") as mf:
	m_text = mf.read()

text = "私には夢がある"
words = nagisa.tagging(text)
print(words)
"""

with open("./janome.txt", encoding="utf-8") as jf:
	jt = jf.read()

str = ""
t = Tokenizer()
for token in t.tokenize(jt):
	if token.surface == "。":
		str += "\n"
	elif token.surface != "\n":
		str += token.surface
		str += " "

print(str)

janome_model = markovify.NewlineText(str)
for i in range(2):
	print(janome_model.make_sentence())
