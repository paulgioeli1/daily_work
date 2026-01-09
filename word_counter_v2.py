sentence = "Wow you made a sentence Wow Wow WOW"

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

counter = 0
counted_words_list = []


for i in range(len(word_list)):  #for every word in the word_list
    word = word_list[i]          #take the first word
    counter = 0              #our counter is 0
    for j in range(len(word_list)): #then, for every word in that list
        if word == word_list[j]:    #compare the first word to all the words
            counter += 1            #If they match, then add one to counter
            counted_words_list.append(word)  
    print(word + " : " + str(counter))    

print(counted_words_list)    