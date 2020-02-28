import markovify
#import nagisa
from janome.tokenizer import Tokenizer

with open("./test.txt", encoding="utf-8") as f:
	text = f.read()

"""
#英文のサンプルを直接マルコフ連鎖にかける
#text_model = markovify.Text(text)
text_model = markovify.NewlineText(text)

for i in range(5):
	print(text_model.make_sentence())
"""

#with open("./janome.txt", encoding="utf-8") as jf:
with open("./sengoku.txt", encoding="utf-8") as jf:
	jt = jf.read()

str = ""
t = Tokenizer()
for token in t.tokenize(jt):
	if token.surface == "。":
		str += "\n"
	elif token.surface != "\n":
		str += token.surface
		str += " "

#print(str)

janome_model = markovify.NewlineText(str)
str = janome_model.make_short_sentence(150)
print(str.replace(" ", ""))
#for i in range(2):
#	print(janome_model.make_sentence())
