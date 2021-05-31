def jml_kuadrad_ganjil(n):
    sum = 0
    for x in range(n):
        if x%2 == 0:
            continue
        sum += x**2
    return sum

print(jml_kuadrad_ganjil(5))