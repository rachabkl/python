class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


# Input from the user
word = input("Enter a word: ")

# Create an object
obj = Reverse(word)

# Display the reversed word
print(obj.reverse_string())