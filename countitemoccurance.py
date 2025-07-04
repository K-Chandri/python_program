from collections import Counter
list1 = ['Chandu','tanj','vani','tanj'] 
count1 = Counter(list1).get("tanj")
print(f'The name Vani appears in the list'
     f' {count1} times')
