words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

def count_vowels(word):
    for word in words:
        list = []
        Sum_of_voyelles = []
        voyelles = ["a", "e", "i", "o", "u", "y"]
        for letter in word:
            if letter in voyelles:
                Sum_of_voyelles.append(letter)
        list.append(word)
        list.append(len(Sum_of_voyelles))
        print(list)
        
count_vowels(words)