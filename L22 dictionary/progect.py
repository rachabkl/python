# test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# print the dictionary
print(test_dict)

# ask the user for a word
word = input("Enter a word: ")

# check and print frequency
if word in test_dict:
    print("Frequency:", test_dict[word])
else:
    print("Word not found in dictionary")