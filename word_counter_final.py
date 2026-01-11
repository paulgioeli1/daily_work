# Word_counter_final

test_string = "You can really really count count count those duplicates count"
test_string = test_string.lower()

deduped_string = dedupe(string)

counts_list = []

for i in range(len(deduped_string)):
    counter = 0
    for j in range(len(test_string)):
        if test_string[j] == deduped_string[i]:
            counter += 1
    counts_list.append(counter)

print(counts_list)
        
        

