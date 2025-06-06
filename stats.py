def get_num_words(input):
    words = input.split() # takes the input from main.py and creates list of words
    total_words = len(words) # reports on how many words are in the list
    # print(f"{total_words} words found in the document")
    return total_words

def get_characters(input):
    characters_dict = {} # initializes empty dictionary
    lowercase = input.lower() # removes symbols and makes all characters lowercase
    character_list = list(lowercase) # list(lowercase) separates out each character in the strings
    # print(character_list) prints each character as a test
    for characters in character_list: # looping through every character in the list
        if characters in characters_dict: # checks whether character in dict already
            characters_dict[characters] += 1 # if in character dict, increment value of respective character key up by 1
        else: 
            characters_dict[characters] = 1 # if not in character dict already, adds it

    # print(characters_dict)
    return characters_dict


def sort_on(input_dict):
        return input_dict["num"]

def sorted_characters(input_dict):
    
    sorted_list = [] # opening blank list
    #Srted_dict = {} # opening blank dictionary
    for character in input_dict: # starting the loop through input dictionary
        if character.isalpha() == True:
            new_dict = {}
            char = character
            num = input_dict[character]
            new_dict = {
                "char": char,
                "num": num
                }
            sorted_list.append(new_dict) 
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
    
    