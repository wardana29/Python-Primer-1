def barisan_ganjil(data):
    data = set(data)
    for i in data:
        for j in data:
            if i == j :
                continue
        if i*j % 2 == 1:
            return True
    return False


print(barisan_ganjil([1,3,5,7,9]))