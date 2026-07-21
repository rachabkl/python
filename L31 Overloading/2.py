class Flashcard : 
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning 
    def __str__(self):
        return self.word + "( " + self.meaning + " )"
flash = []
print("Welcome to Flashcard Application")
while True :
    word = input("Enter the word : ")
    meaning = input("Eter it's meaning : ")
    flash.append(Flashcard(word,meaning))
    option = int(input("Enter 0 to add another Flashcard or 1 to stop:"))
    if option == 1:
        break

print("\n Your Flashcards")
for card in flash:
    print(">",card)    
