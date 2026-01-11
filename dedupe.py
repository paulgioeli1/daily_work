def dedupe(sentence): #must take a string
    sentence = sentence.lower()

    word_list = []
    current_word = ""

    sentence = sentence + " " #We're using blank spaces to find words, and the last word has no space after it!

    for a in sentence:
        if a != " ":
            current_word = current_word + a
        else:
            word_list.append(current_word)
            current_word = ""

    deduped_list = []

    deduped_list.append(word_list[0])
    word_list = word_list[1:]

    print(deduped_list)
    print(word_list)

    for i in range(len(word_list)):
        counter = 0
        for j in range(len(deduped_list)):
            if word_list[i] == deduped_list[j]:
                counter += 1
        if counter == 0:        
            deduped_list.append(word_list[i])
    
    return(deduped_list)

if __name__== "__main__":

    # OK, with a little more sleep and a new file, let's do this again.
    # Create a function that can dedupe the words in a string.

    sentence = "Wow you wrote a sentence wow wow wow sEnTeNcE"
    print(sentence)

    #let's minimize all the letters, so that way they actually count correctly.
    sentence = sentence.lower()
    print(sentence)
    print("Good job, you made all the letters lowercase!")

    #Now, let's put all those words into a list we can then manage
    word_list = []
    current_word = ""

    sentence = sentence + " " #We're using blank spaces to find words, and the last word has no space after it!

    for a in sentence:
        if a != " ":
            current_word = current_word + a
        else:
            word_list.append(current_word)
            current_word = ""

    print(word_list)
    print("Groovy, you put all of them into a list!")
    print("#---------------------------------------------------------#")

    # Now that we have them in a list, let's dedupe the list.
    # We'll take the first word and put it into our deduped list.
    # We'll then remove that element from the list
    # We'll then take each word that follows, and check it against every word in deduped list.
    # If it's not there, we add it.
    # If it is there, we break.
    # Let's give it a try

    deduped_list = []

    deduped_list.append(word_list[0])
    word_list = word_list[1:]

    print(deduped_list)
    print(word_list)

    for i in range(len(word_list)):
        counter = 0
        for j in range(len(deduped_list)):
            if word_list[i] == deduped_list[j]:
                counter += 1
        if counter == 0:        
            deduped_list.append(word_list[i])

    print(deduped_list)

    #great, let's make it a function now that we know it works:

    # Let's show this runs

    test = "this string string HaS bEEn run run been been been"

    print(dedupe(test))