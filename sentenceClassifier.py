#sentenceClassifier.py
import sys
import string

class sentenceClassifier():
	def __init__(self, sentence):
		self.compound_words= {'for', 'and', 'nor', 'but', 'or', 'yet', 'so'}
		self.complex_words = {'after', 'although', 'as', 'because', 'before', 'even', 'though', 'if', 'since', 'though', 'unless', 'until', 'when', 'whenever', 'whereas', 'wherever', 'while'}
		result = self.findCommonWord(sentence)

	def findCommonWord(self, sentence):
		compound_acc = 0
		complex_acc = 0
		
		for i in sentence:
			if i in self.compound_words:
				compound_acc += 1
			if i in self.complex_words:
				complex_acc += 1
		result = self.classifySentence(compound_acc, complex_acc)
		return result

	def classifySentence(self, compound_acc, complex_acc):
		simple = "simple sentence"
		compound_sent = "compound sentence"
		complex_sent = "complex sentence"
		compound_complex = "compound-complex sentence"

		if compound_acc == 0 and complex_acc == 0:
			return simple
		elif compound_acc == 0 and complex_acc == 1:
			return complex_sent
		elif compound_acc == 1 and complex_acc == 0:
			return compound_sent
		elif compound_acc == 1 and complex_acc == 1:
			return compound_complex

def main():
	sentence = input("Input sentence: ")
	sentence = sentence.lower()
	punctuation = set(string.punctuation)

	for i in sentence:
		if i in punctuation:
			sentence.strip(i)

	sentence_list = sentence.split()
	sentenceClassifier(sentence_list)

if __name__ == '__main__':
	main()