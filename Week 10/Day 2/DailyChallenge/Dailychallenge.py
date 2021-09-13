#with deep_translator moudle
from deep_translator import GoogleTranslator
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
english_words = []
for word in french_words:
    translated = GoogleTranslator(source='french', target='english').translate(word)
    english_words.append(translated)
print(english_words)

#with googletrans moudle
from googletrans import Translator
translator = Translator()
french_words = translator.translate(["Bonjour", "Au revoir", "Bienvenue", "A bientôt"])
english_words = []
for word in french_words:
    english_words.append(word.text)
print(english_words)
