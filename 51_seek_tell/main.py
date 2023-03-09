'''
f = open('myfile.txt', 'r')
f.read()
print(f.tell(), 'current position')                               #tell current position
f.seek(14)                                      #skip 1 to 14 and read next 5 characters
print(f.tell())                               #tell current position
print(f.read(5))
print(f.tell())                               #tell current position-->19
'''

with open('myfile2.txt', 'w') as f:
    f.write('hello world')
    f.truncate(7)

with open('myfile2.txt', 'r') as f:
    print(f.read())