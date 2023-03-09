'''
f = open('myfile.txt','r')
while True:
    line = f.readline()
    print(line)
    if not line:
        break
    print(line)
'''

'''
i=0
f = open('myfile.txt','r')
while True:
    line = f.readline()
    if not line:
       break
    i=i+1
    m0 = line.split(',')[0]
    m1 = line.split(',')[1]
    m2 = line.split(',')[2]
    print(f'Marks of student {i} is {m0}')
    print(f'Marks of student {i} is {m1}')
    print(f'Marks of student {i} is {m2}')
    print(line)
'''

# find difference between writelines and write
f = open('myfile2.txt','w')
# lines = 'my name si paras'
# f.write(lines)
lines = ['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5\n']
f.writelines(lines)
f.close()


