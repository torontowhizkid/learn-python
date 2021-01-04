from PyDictionary import PyDictionary
word=input("Enter your word: ")
print("Meaning = ", PyDictionary().meaning(word))
print("Synonym = ", PyDictionary().synonym(word))
print("Antonym = ", PyDictionary().antonym(word))
print("French = ", PyDictionary().translate(word, 'fr'))
print("Tamil = ", PyDictionary().translate(word, 'ta'))
