class AnagramChecker():
    def __init__(self,word_list):
        self.word_list = word_list

    def is_valid_word(self,word):
        return True if word in self.word_list else False
    
    def is_anagram(self,word1,word2):
        if word1 == word2:
            return False
        elif sorted(word1) == sorted(word2):
            return True
        else:
            return False      

    def get_anagrams(self,word):
        word = word.lower()
        anagrams_list = []
        for line in self.word_list:
            if self.is_anagram(word,line.lower()):
                anagrams_list.append(line.lower())
        return anagrams_list


word_list = open('GIT\Week 10\Day 5\Exercises\Anagram Checker/sowpods.txt','r').read().splitlines()
anagram = AnagramChecker(word_list)
# print(anagram.word_list)
print(anagram.is_valid_word('ABACTERIAL'))
print(anagram.is_anagram('wadu','duaw'))
print(anagram.get_anagrams('meat'))