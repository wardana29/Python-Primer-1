from random import randrange

def pilihan(data):
    x = randrange(0,len(data))
    return data[x]


print(pilihan([10,9,8,7,6,5]))