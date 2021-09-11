import re
paragraph = '''Panchaka is a Hindu festival,
the last five days of the month of Kartika are traditionally known as the Bhishma Panchaka or the Vaka Panchaka,
According to the epic poem Jagamohana Ramayana,
written by Balarama Dasa, it is said that if one is capable, one should fast from certain foods on the Bhishma Panchaka for the pleasure of the Vishnu,
The Padma Purana say that one pleases Vishnu and makes spiritual advancement.'''
print(f"This paragraph contains {len(paragraph)} characters")
print(f"This paragraph contains {len(paragraph.split(','))} sentences")
words = len(re.findall(r'\w+', paragraph))
print(f"This paragraph contains {words} words")
words = re.findall(r'\w+', paragraph)
words = len(list(dict.fromkeys(words)))
print(f"This paragraph contains {words} unique words")