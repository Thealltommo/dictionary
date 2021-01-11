import json #  allows the json file ext to be used
from difflib import get_close_matches #  allows words to be compared for similarities

data = json.load(open("data.json")) # uses the data.json files contents

def translate(word): #  define a function that searches through the data.json file
    word = word.lower() #  lowers the case in case of mixed case inputs
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0: #  searches for words that may be similar to input
        yn = input ("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0]) #  offers an alternative
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]] #  returns first closest in the list of close matches
        elif yn == "N" or "n":
            return "Word does not exist, please check again."
        else:
            "We didn't understand your query."
    else:        
        return "Word is not recognised, please try another"

word = input("Enter word: ") #  choose word to be searched

output = (translate(word)) # call translate function to find word 

if type(output) == list:
    for item in output:
        print(item) #  gives the output a more user friendly view instead of presenting as a python list
else:
    print(output)