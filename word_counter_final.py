# Word_counter_final
from dedupe import dedupe

test_string = "You can really really count count count those duplicates count"
test_string = test_string.lower()


word_list = []
current_word = ""

test_string = test_string + " " # I should create this as a function

for a in test_string:
    if a != " ":
        current_word = current_word + a
    else:
        if current_word != "":
            word_list.append(current_word)
            current_word = ""


deduped_string = dedupe(test_string)

counts_list = []

for i in range(len(deduped_string)):
    counter = 0
    for j in range(len(word_list)):
        if word_list[j] == deduped_string[i]:
            counter += 1
    counts_list.append(counter)

print(deduped_string)
print(counts_list)
        
        

