from collections import Counter


class Text():
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        times = 0
        text_list = (self.text.split())
        for i in text_list:
            print(i)
            if i == word:
                times += 1
        if times > 0:
            print(f'The word "{word}" appears {times} times.')
        else:
            print(f'"{word}" is not in the sentance')

    def most_common(self):
        times = 0
        text_list = (self.text.split())
        counter = Counter(text_list)
        print(type(counter))
        most_occur = counter.most_common()
        print(f'The most common word is "{most_occur[0][0]}".')

    def unique_words(self):
        times = 0
        text_list = (self.text.split())
        counter = Counter(text_list)
        print((counter))
        most_occur = counter.most_common()
        unique_list = []
        for i in most_occur:
            unique_list.append(i[0])
        print(unique_list)


sen = Text("hello word world world")
print(sen.text)
# sen.word_frequency("hello")
# sen.most_common()
sen.unique_words()


class Text_Modifications(Text):
    def __init__(self, text):
        self.text = text

    def remove_punc(self):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in self.text:
            if i in punc:
                self.text = self.text.replace(i, "")
        return self.text

    def remove_stopwords(self):
        stopword_list = []
        for line in open("Stopwords.txt"):
            line = line.strip()
            stopword_list.append(line)

        for i in self.text:
            if i in stopword_list:
                self.text = self.text.replace(i, "")
        return self.text


f = open("the_stranger.txt")
a= Text_Modifications(f.read())

print(a.remove_punc())
print(a.remove_stopwords())
