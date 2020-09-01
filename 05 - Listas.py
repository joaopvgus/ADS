abc = 'String'

print(abc[-1])

people = ['Jorge', 'Tom', 'Jerry', 'Brutus']
people[0] = 'Mike'
print(*people)  # show all the elements inside the list/array
people.append('Toby')  # add 'Toby' at the end of 'people'

list1 = ['John', 'Leon']
people.extend(list1)  # add a list at the end of another list
people.insert(0, 'Ana')  # add 'Ana' in the beginning and push all the other elements
people.remove('Tom')  # don't really have to explain'
print(*people)

# people.clear() # erase all the elements inside the list
# people.pop() # erase a random element
print(people.index('Leon'))  # prints the location of 'Tom'
print(people.count('Jerry'))  # prints how many 'Jerry's' exist in the list
people.sort()  # set's the list in alfabetical/crescent order
people.reverse()  # reverses the order of the list

people2 = people.copy()
people2.insert(0, 'Karen')

print('people = ' + str(people))
print('people2 = ' + str(people2))

coordinates = (1, 2)  # that's a tuple, it's like a list, but it's immutable
