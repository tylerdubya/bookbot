from stats import get_num_words # importing get_num_words function from stats.py
from stats import get_characters # importing get_characters function from stats.py
from stats import sorted_characters # importing sorted_characters function from stats.py
from stats import sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath): # creating function definition w/ input being filepath
    with open(filepath) as f: # with function to open a filepath and read contents
        file_contents = f.read()
        return (file_contents)
    
text = get_book_text(sys.argv[1]) # using get_book_text to store text as string from filepath

word_num = get_num_words(text) # calling get_num_words with text input to get word_number

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_num} total words") # reporting number of words in text

characters_dict = get_characters(text) # calling get_characters function w/ input text to get dictionary of characters and occurences

#print(characters_dict) # reporting character key/value pairs

sorted_dict = sorted_characters(characters_dict)
print("--------- Character Count -------")
for group in sorted_dict:
      print(f"{group['char']}: {group['num']}")
print("============= END ===============")






