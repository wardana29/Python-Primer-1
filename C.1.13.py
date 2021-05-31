def pseudocode(list):
    array=[]
    for i in range(0, len(list)):
        array.append(list[len(list)-i-1])
    return array

print(pseudocode([0,1,2,3]))
