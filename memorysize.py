import sys
a = ['hot', 'cold', 'cool']
b = ('hot', 'cold', 'cool')
c = {'hot', 'cold' , 'cool'}
print(f'The memory size of a list is 'f'{sys.getsizeof(a)}')
print(f'The memory size of a set is 'f'{sys.getsizeof(b)}')
print(f'The memory size of a tuple is 'f'{sys.getsizeof(c)}')
