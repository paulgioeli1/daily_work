#Create a word counter from a string

#First thing: I'm pretty sure a space is an ASCII character, let's see

# char = " "

# if char == " ":
#     print("Yep, it's a character")
# else:
#     print("nope")

#Great. If a space is a character, then we can find it in a string.
#How do I return the index of an item in an iterable?
#Cool, ya figured it out.

# list = ["a", "b", "c", "d"]

# print(list.index("b"))


sentence = "Wow you made a sentence Wow Wow WOW"

for i in sentence:
    if i == " ":
        print(sentence.index(i))

# Wait, what if I just iterated through, and placed each word in a list? That's probably simpler
# for each character in sentence
# if the character isn't blank, then concatenate it to a string
# if it is blank, then take whatever that variable is and add it to a list.
        
# damn, the last word didn't show. Maybe I can do some sort of pre-processing, 
# like throwing appending a blank to the end of the string at the end?
# That seems cheap and stupid, but it'll run.


word = ""
word_list = []

sentence = sentence + " "
sentence = sentence.lower()

print(sentence)

for i in sentence:
    if i != " ":
        word = word + i
    else:
        word_list.append(word)
        word = ""

print(word_list)

# cool, we've got our word list.
# To create the counter, let's put the first word as a variable
# Then loop through the text and everytime an element matches, we add to the counter
# Then print the word and the counter? yeah that should work

counter = 0
counted_words_list = []
for i in range(len(word_list)):  #for every word in the word_list
    word = word_list[i]  #take the first word
    counter = 0             #our counter is 0
    for i in range(len(counted_words_list))
    for j in range(len(word_list)): #then, for every word in that list
        if word == word_list[j]:    #compare the first word to all the words
            counter += 1            #If they match, then add one to counter
            counted_words_list.append(word)            #Then add that word to a counted_words list
    
    # print(word + " : " + str(counter))

#Next Steps:

# -1- dedupe the list
# so, one way (probably a dumb way) to dedupe is to do the whole counting thing, and then create a "counted_words" list that can then hold the words we already counted
# and if that word is in that list, we don't nee to output it.

#this file is now super gross, starting another file that's clean