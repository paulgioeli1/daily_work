#deduping a list

list1 = ['a', 'b', 'c', 'd', 'a', 'a', 'b', 'b', 'e']


#Take element
# if first element, place in new list
# if not first element, compare to all elements in new list
# if that element is equal to ANY member of new list, then don't add to new list
# if that element isn't equal to any member of new list, then add to new list.
# Great, here we go

# new_list = []
# inList = True

# for i in range(len(list1)):
#     if i == 0:
#         new_list.append(list1[i])
#     else:
#         for j in range(len(new_list)):
#             if list1[i] == new_list[j]:
#                 inList = True
#             else:
#                 inList = False
#                 if inList == False:
#                     new_list.append(list[i])

# print(new_list)

#---------------------------------------# Let's try again
letter_list = ['a', 'b', 'c', 'd', 'a', 'a', 'b', 'b', 'e']
dedupe_list = []

for i in range(len(letter_list)):
    if i == 0:
        dedupe_list.append(letter_list[i])
    else:
        print(letter_list[i])
        for j in range(len(dedupe_list)):
            print(letter_list[i])
            print(dedupe_list[j])
            if letter_list[i] == dedupe_list[j]:
                print("Matches, no need to add")
            else:
                dedupe_list.append(letter_list[i])


print(dedupe_list)