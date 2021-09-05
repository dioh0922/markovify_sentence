from janome.tokenizer import Tokenizer		#品詞分解用モジュール
import sentence_module

#事前に品詞分解した文字列に書き出す(実環境ではメモリ不足しがち)
def generate_tokenized_text():
	tokenizer = Tokenizer()
	chn_text = sentence_module.read_file_text("sonshi_pick.txt")
	chn_str = split_part_of_speach(chn_text)
	with open("token_chn.txt", "w", encoding="utf-8") as fp:
		fp.write(chn_str)

	jpn_text = sentence_module.read_file_text("sonshi_jpn_pick.txt")
	jpn_str = split_part_of_speach(jpn_text)
	with open("token_jpn.txt", "w", encoding="utf-8") as fp:
		fp.write(jpn_str)

#品詞分解してスペースで区切った文字列を返す処理
def split_part_of_speach(text):
	tokenizer = Tokenizer()
	str = ""
	for token in tokenizer.tokenize(text):
		if token.surface == "。":	#。で1行とする
			str += "\n"
		elif token.surface != "\n":
			str += token.surface
			str += " "	#スペースで品詞ごとに区切る

	return str
