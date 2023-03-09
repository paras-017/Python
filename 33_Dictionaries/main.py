dict = {
    'name':'paras',
    'age':18,
    'spoon':'Object'
}

# print(dict['name2'])                         #gives error if not found
# print(dict.get('name2'))                         #gives none if not found

# print(dict.keys())                                          #gives all keys  present in dictionary 
# print(dict.values())                                          #gives all values  present in dictionary

'''
for key in dict:
    # print(dict[key])
    print(f'The value corresponding to the key {key} is {dict[key]}')
'''


''''
print(dict.items())
for key,value in dict.items():
    print(f'The value corresponding to the key {key} is {value}')
'''