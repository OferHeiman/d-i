import string
import re
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')

class Text():
    def __init__(self,text_file) -> None:
        self.text_file = text_file
    
    def word_freq(self,string):
        text = open(self.text_file,'r')
        text.seek(0)
        num_freq = re.findall(string + ' ', text.read())
        if len(num_freq) == 0:
            text.close()
            return None
        else:
            print(f"The number of times the word '{string}' occurred is: {len(num_freq)}")
            text.close()
            return len(num_freq)
    
    def most_common_word(self):
        word_dict = {}
        text = open(self.text_file,'r')
        text.seek(0)
        currentword = ''
        for line in text:
            for word in line:
                if word.isalpha():
                    currentword = currentword + word
                else:
                    if currentword in word_dict:
                        word_dict[currentword] += 1
                    else:
                        word_dict[currentword] = 1
                    currentword = ''
        word_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1],reverse=True)}
        text.close()
        return list(word_dict)[1]
    
    def unique_words(self):
        word_list = []
        text = open(self.text_file,'r')
        text.seek(0)
        currentword = ''
        for line in text:
            for char in line:
                if char.isalpha():
                    currentword = currentword + char
                else:
                    if not currentword in word_list:
                        word_list.append(currentword)
                    currentword = ''
        text.close()
        return word_list
        
    @classmethod
    def from_file(self,txt):
        return Text(txt)

class TextModification(Text):
    def __init__(self, text_file) -> None:
        super().__init__(text_file)
    
    def no_punctuation(self):
        text = open(self.text_file)
        text.seek(0)
        no_punc = text.readlines()
        text.close()
        for x in range(len(no_punc)):
            for char in no_punc[x]:
                if char in string.punctuation:
                    no_punc[x] = no_punc[x].replace(char,'')
        text = open(self.text_file, "w")
        text.write("".join(no_punc))
        text.close()
        return open(self.text_file).read()
    
    def no_stop_words(self):
        text = open(self.text_file)
        text.seek(0)
        no_stop_word = text.readlines()
        text.close()
        for x in range(len(no_stop_word)):
            current_line = no_stop_word[x].split()
            for y in range(len(current_line)):
                if current_line[y] in stopwords.words('english'):
                    current_line[y] = current_line[y].replace(current_line[y],'')
                    no_stop_word[x] = " ".join(current_line).strip()+'\n'
        text = open(self.text_file,'w')
        text.write("".join(no_stop_word))
        text.close()
        return open(self.text_file).read()
    
    def no_special_characters(self):
        string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        text = open(self.text_file)
        text.seek(0)
        no_punc = text.readlines()
        text.close()
        for x in range(len(no_punc)):
            for char in no_punc[x]:
                if string_check.search(char):
                    no_punc[x] = no_punc[x].replace(char,'')
        text = open(self.text_file, "w")
        text.write("".join(no_punc))
        text.close()
        return open(self.text_file).read()


word = Text('GIT\Week 10\Day 4\Daily Challenge/the_stranger.txt')
print(word.word_freq('the'))
print(f"The most common word is: {word.most_common_word()}")
print(f"List of unique words: \n{word.unique_words()}")
print(Text.from_file(open('GIT\Week 10\Day 4\Daily Challenge/the_stranger.txt')))
text = TextModification('GIT\Week 10\Day 4\Daily Challenge/the_stranger.txt')
text.no_punctuation()
text.no_stop_words()
text.no_special_characters()