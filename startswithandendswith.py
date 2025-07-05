list1 = ['lemon','orange','apple','apricot']
new_list1 = [j for j in list1 if j.startswith('a')]
new_list2 = [i for i in list1 if i.endswith('e')]
print(new_list1)
print(new_list2)