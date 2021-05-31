def minmax(data):
    terkecil = terbesar = data[0]
    for a in data:
        if terkecil > a:
            terkecil = a
        if terbesar < a:
            terbesar = a
    return (terkecil, terbesar)


print(minmax([5,14,25,26,2,1,9,8,4,5,7,5,2,1,1,-10,0,100]))