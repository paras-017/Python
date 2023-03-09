'''
f = open('myfile.txt', 'r')
newfile = open('myfile2.txt', 'w') 
print(f)
text = f.read()
print(text)
# f.close() 
'''
f = open('myfile2.txt', 'a')
f.write('hello world ')
f.close()