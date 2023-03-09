# print('a'*6) = aaaaaa



'''
try:
    a = input('Enter a number')
    for i in range(1,11):
        print(f'{a} X {i} = {int(a)*i}')
except:
    print('invalid input')
'''

try:
    num=int(input('Enter a number \n'))
    arr = [6,9]
    print(arr[num])
except ValueError:
    print('value is not an integer')
except IndexError:
    print('index out of range')


