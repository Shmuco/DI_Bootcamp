class Anagram_checker():
    def __init__(self, use_in):
        self.use_in = use_in.upper()
        self.words = []
        f = open('sowpods.txt', 'r')
        li = f.readlines()

        for lines in li:
            self.words.append(lines.strip())
        


    def is_valid_word(self):
        if self.use_in in self.words:
            return True

        else:
            return False

    def get_anagrams(self):
        anagram_list = []
        for i in self.words:
            if (sorted(self.use_in.upper())==sorted(i)):
                if i != self.use_in.upper():
                    anagram_list.append(i.lower())
        return anagram_list
        


            
        



