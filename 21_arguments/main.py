def average1(a=1,b=3):
    print("The average is",(a+b)/2)
average1(b=100)


def average2(*num):
    sum = 0 
    for i in num:
        sum +=i
    print('average is', sum/len(num))
average2(1,2,3,4,5,6)


def average3(**dic):
    print(dic['Oname'],'owns a', dic['pet'])
average3(Oname='paras', pet='cat')