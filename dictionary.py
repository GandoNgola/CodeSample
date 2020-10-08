import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(word, data.keys())[0])
        if yn == "Y" or "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or "n":
            return "Sorry, we didn't find what you were looking for. Or try to check your spelling."
        else:
            return "the word doesn't exist, Porra!"
    else:
        return "The word is not in the dictionary!\n Try another word!"

word = input("enter a word: ")
print(translate(word))
